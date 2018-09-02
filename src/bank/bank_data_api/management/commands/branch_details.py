from django.core.management import BaseCommand
from bank_data_api.models import Branch, Bank
import csv

class Command(BaseCommand):
    def handle(self, *args, **options):
        with open('bank_data_api/csv_files/bank_branches.csv') as csvfile:
            readCSV = csv.reader(csvfile, delimiter=',')
            # remove First Line(header)
            next(csvfile)
            for row in readCSV:
                print(row[1])

                bank_obj = Bank.objects.get(bank_id = row[1])

                branch, create = Branch.objects.get_or_create(bank = bank_obj)
                branch.ifsc = row[0]
                branch.branch = row[2]
                branch.address = row[3]
                branch.city = row[4]
                branch.district = row[5]
                branch.state = row[6]
                branch.save()

