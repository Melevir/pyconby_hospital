from django.core.management.base import BaseCommand

from registry import factories


class Command(BaseCommand):
    def handle(self, *args, **options):
        self.create_patients()
        self.create_doctors()
        self.create_visits()

    def create_patients(self):
        for _ in range(10):
            factories.PatientFactory().save()

    def create_doctors(self):
        pass

    def create_visits(self):
        pass
