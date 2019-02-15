from django.db import models


class Patient(models.Model):
    name = models.CharField(max_length=512)

    def __str__(self):
        return self.name


class Doctor(models.Model):
    name = models.CharField(max_length=512)

    def __str__(self):
        return self.name


class Visit(models.Model):
    patient = models.ForeignKey('Patient', on_delete=models.CASCADE, related_name='visits')
    doctor = models.ForeignKey('Doctor', on_delete=models.CASCADE, related_name='visits')
    room_num = models.PositiveSmallIntegerField()
    visited_at = models.DateTimeField()

    def __str__(self):
        return '{0} к {1} в {2} (кабинет {3})'.format(self.patient, self.doctor, self.visited_at, self.room_num)
