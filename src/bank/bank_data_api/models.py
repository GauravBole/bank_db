from django.db import models

# Create your models here.

class Bank(models.Model):
    """ Store a Bank Name and Bank Id """

    bank_name = models.CharField(max_length=100, null=False, blank=False)
    bank_id = models.IntegerField()

    def __str__(self):
        return str(self.bank_id)


class Branch(models.Model):
    """Stotre Branch Data """

    ifsc = models.CharField(max_length=100, null=False, blank=False)
    bank = models.ForeignKey(Bank, on_delete=models.SET_NULL, null=True)
    branch = models.CharField(max_length=100, null=False, blank=False)
    address = models.CharField(max_length=200, null=False, blank=False)
    city = models.CharField(max_length=100, null=False, blank=False)
    district = models.CharField(max_length=100, null=False, blank=False)
    state = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return self.bank.bank_id

