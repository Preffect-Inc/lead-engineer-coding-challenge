from django.core.management.base import BaseCommand
from app.models import User
import csv

class Command(BaseCommand):
    help = 'Load users from CSV'

    def handle(self, *args, **options):
        with open('data/users.csv') as f:
            r = csv.reader(f)
            header = next(r)
            for row in r:
                User.objects.update_or_create(
                    user_id=row[0],
                    defaults={
                        'name': row[1],
                        'email': row[2],
                        'signup_date': row[3],
                        'age': int(row[4]),
                        'height_cm': int(row[5]),
                        'weight_kg': int(row[6]),
                        'activity_level': row[7],
                        'health_goals': row[8],
                    }
                )
        self.stdout.write(self.style.SUCCESS('Users loaded successfully'))
