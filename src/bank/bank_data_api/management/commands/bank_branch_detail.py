from django.core.management import BaseCommand

import csv

class Command(BaseCommand):
    def handle(self, *args, **options):
        with open('bank_data_api/csv_files/bank_branches.csv') as csvfile:
            readCSV = csv.reader(csvfile, delimiter=',')
            i = 0
            for row in readCSV:
                print(row)