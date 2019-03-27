from django.db import models
from django.db.models.deletion import PROTECT
from edc_model.models import BaseUuidModel
from edc_sites.models import SiteModelMixin
from edc_visit_schedule.model_mixins import (
    OffScheduleModelMixin,
    OnScheduleModelMixin,
    SubjectOnScheduleModelMixin,
)
from edc_visit_tracking.model_mixins import VisitModelMixin

from ..model_mixins import RequisitionModelMixin
from edc_identifier.model_mixins.subject_identifier_model_mixins import (
    UniqueSubjectIdentifierFieldMixin,
)
from edc_identifier.managers import SubjectIdentifierManager
from edc_consent.model_mixins.consent_model_mixin import ConsentModelMixin
from edc_consent.field_mixins.personal_fields_mixin import PersonalFieldsMixin
from edc_consent.field_mixins.identity_fields_mixin import IdentityFieldsMixin
from edc_registration.model_mixins.updates_or_creates_registered_subject_model_mixin import (
    UpdatesOrCreatesRegistrationModelMixin,
)
from edc_visit_schedule.model_mixins.visit_schedule_model_mixins import (
    VisitScheduleMethodsModelMixin,
    VisitScheduleFieldsModelMixin,
)
from edc_reference import ReferenceModelConfig, site_reference_configs
from edc_metadata.model_mixins.creates.creates_metadata_model_mixin import (
    CreatesMetadataModelMixin,
)


site_reference_configs.registry = {}
reference = ReferenceModelConfig(
    name="edc_lab.subjectrequisition.panel", fields=["panel"]
)
site_reference_configs.register(reference)
reference = ReferenceModelConfig(name="edc_lab.CrfOne", fields=["f1"])
site_reference_configs.register(reference)


class SubjectRequisitionManager(models.Manager):
    def get_by_natural_key(
        self, requisition_identifier, subject_identifier, report_datetime
    ):
        subject_visit = SubjectVisit.objects.get(
            subject_identifier=subject_identifier, report_datetime=report_datetime
        )
        return self.get(
            requisition_identifier=requisition_identifier, subject_visit=subject_visit
        )


class SubjectVisit(
    VisitModelMixin, CreatesMetadataModelMixin, SiteModelMixin, BaseUuidModel
):
    def update_reference_on_save(self):
        pass


class SubjectRequisition(RequisitionModelMixin, BaseUuidModel):

    subject_visit = models.ForeignKey(SubjectVisit, on_delete=PROTECT)

    objects = SubjectRequisitionManager()

    def natural_key(self):
        return (self.requisition_identifier,) + self.subject_visit.natural_key()

    natural_key.dependencies = ["edc_lab.simplsubjectvisit", "sites.Site"]

    @property
    def visit(self):
        return self.subject_visit

    def update_reference_on_save(self):
        pass


class OnSchedule(OnScheduleModelMixin, BaseUuidModel):

    pass


class OffSchedule(OffScheduleModelMixin, BaseUuidModel):

    pass


class DeathReport(UniqueSubjectIdentifierFieldMixin, SiteModelMixin, BaseUuidModel):

    objects = SubjectIdentifierManager()

    def natural_key(self):
        return (self.subject_identifier,)


class SubjectConsent(
    ConsentModelMixin,
    PersonalFieldsMixin,
    IdentityFieldsMixin,
    UniqueSubjectIdentifierFieldMixin,
    UpdatesOrCreatesRegistrationModelMixin,
    SiteModelMixin,
    # OnScheduleModelMixin,
    SubjectOnScheduleModelMixin,
    VisitScheduleFieldsModelMixin,
    VisitScheduleMethodsModelMixin,
    BaseUuidModel,
):

    objects = SubjectIdentifierManager()

    def natural_key(self):
        return (self.subject_identifier,)
