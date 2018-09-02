from django.core.management import BaseCommand
from bank_data_api.models import Bank
import csv


class Command(BaseCommand):
    def handle(self, *args, **options):
        with open('bank_data_api/csv_files/bank_branches.csv',encoding="utf-8") as csvfile:
            readCSV = csv.reader(csvfile, delimiter=',')

            # remove First Line(header)
            next(csvfile)
            for row in readCSV:

                banks = Bank.objects.filter(bank_id=row[1],bank_name = row[7])
                if banks:
                    print("bank id--->",row[1])

                else:
                    banks = Bank.objects.create(bank_id=row[1],bank_name = row[7])
