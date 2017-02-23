from django.apps import apps as django_apps
from django.contrib.auth.decorators import login_required
from django.urls.base import reverse
from django.utils.decorators import method_decorator

from edc_base.view_mixins import EdcBaseViewMixin
from edc_dashboard.forms import SearchForm as BaseSearchForm
from edc_dashboard.view_mixins import AppConfigViewMixin
from edc_dashboard.views import ListboardView
from edc_dashboard.wrappers.model_wrapper import ModelWrapper

app_name = 'edc_lab'
app_config = django_apps.get_app_config(app_name)


class BoxItemModelWrapper(ModelWrapper):

    model_name = app_config.box_item_model
    next_url_name = app_config.box_listboard_url_name
    next_url_attrs = {
        'edc_lab.boxitem': ['box_identifier']}
    url_instance_attrs = ['box_identifier']

    @property
    def human_readable_identifier(self):
        return self._original_object.human_readable_identifier

    @property
    def box_identifier(self):
        return self._original_object.box.box_identifier


class SearchForm(BaseSearchForm):

    action_url_name = app_config.box_listboard_url_name


class BoxListboardView(AppConfigViewMixin, EdcBaseViewMixin,
                       ListboardView):

    action = None
    action_url_name = None
    app_config_name = 'edc_lab'
    empty_queryset_message = 'No items have been added to this box'
    listboard_url_name = app_config.box_listboard_url_name
    model = django_apps.get_model(*app_config.box_item_model.split('.'))
    box_model = django_apps.get_model(*app_config.box_model.split('.'))
    model_wrapper_class = BoxItemModelWrapper
    navbar_item_selected = 'pack'
    navbar_name = 'specimens'
    paginate_by = 10
    search_form_action_url_name = app_config.box_listboard_url_name
    search_form_class = SearchForm
    ordering = ('-position', )

    manage_box_item_url_name = '{}:manage_box_item_url'.format(app_name)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._box = None

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    @property
    def search_form(self):
        self.search_form_class.action_url_name = (
            self.search_form_action_url_name or app_config.box_listboard_url_name)
        return self.search_form_class

    def get_template_names(self):
        return [django_apps.get_app_config(
            self.app_config_name).box_listboard_template_name]

    @property
    def box(self):
        if not self._box:
            try:
                self._box = self.box_model.objects.get(
                    box_identifier=self.kwargs.get('box_identifier'))
            except self.box_model.DoesNotExist:
                self._box = None
        return self._box

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        box_identifier = self.kwargs.get('box_identifier')
        context.update(
            listboard_url=reverse(
                django_apps.get_app_config('edc_lab').box_listboard_url_name,
                kwargs={'box_identifier': box_identifier}),
            pack_listboard_url_name=app_config.pack_listboard_url_name,
            box_identifier=box_identifier,
            box=self.box,
            manage_box_item_url_name=self.manage_box_item_url_name,
            empty_queryset_message=self.empty_queryset_message,
            action=self.action,
            action_url_name=self.action_url_name,
            rendered_box=self.rendered_box(self.box))
        return context

    def get_queryset_filter_options(self, request, *args, **kwargs):
        """Returns filter options applied to every
        queryset.
        """
        return {'box': self.box}

    def rendered_box(self, box=None):
        box = '<table class="table table-condensed table-hover">'
        for _ in range(1, box.box_type.down):
            box += '<tr>'
            for column in range(1, box.box_type.across):
                box += '<td><button class="btn btn-default btn-sm">{}</button></td>'.format(
                    column)
            box += '</tr>'
        box += '</table>'
        return box
