from django_offline.site_offline_models import site_offline_models

site_offline_models.register_for_app(
    'edc_lab', exclude_models=['edc_lab.panel'])
