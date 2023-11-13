import csv
from django.core.management.base import BaseCommand
from hero.models import Superhero

class Command(BaseCommand):
    #record = 'Export data to CSV file'

    def handle(self, *args, **options):
        # Specify the CSV file path
        csv_file_path = "records.csv"

        # Get all records from YourModel
        records = Superhero.objects.all()

        # Write records to CSV file
        with open(csv_file_path, mode='w', newline='') as file:
            writer = csv.writer(file)
            
            # Write header
            writer.writerow(['ID', 'name', 'identity', 'description', 'strengths', 'weaknesses'])  # Add your model fields here

            # Write records
            for record in records:
                writer.writerow([record.id, record.name, record.identity, record.description, record.strengths, record.weaknesses])  # Add your model fields here

        self.stdout.write(self.style.SUCCESS(f'Data exported to {csv_file_path}'))