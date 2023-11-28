# your_app/management/commands/import_data.py

import csv
from django.core.management.base import BaseCommand
from hero.models import Superhero  # Import your model

class Command(BaseCommand):
    #help = 'Import data from CSV file'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, help='Path to the CSV file')

    def handle(self, *args, **options):
        csv_file_path = options['csv_file']

        # Read records from CSV file
        with open(csv_file_path, mode='r') as file:
            reader = csv.DictReader(file)

            for row in reader:
                # Assuming your model fields have the same names as CSV headers
                your_model_instance = Superhero(
                    #ID=row['ID'],
                    name=row['name'],
                    identity=row['identity'],
                    description=row['description'],
                    strengths=row['strengths'],
                    weaknesses=row['weaknesses']
                )
                your_model_instance.save()

        self.stdout.write(self.style.SUCCESS('Data imported successfully'))
