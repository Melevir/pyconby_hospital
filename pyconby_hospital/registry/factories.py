import factory
from . import models


class PatientFactory(factory.Factory):
    class Meta:
        model = models.Patient

    name = factory.Faker('name')
