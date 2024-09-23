from django.db import models

class Patient(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    birth_date = models.DateField()
    prontuario = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

