from django.core.management.base import BaseCommand
from storage.models import UploadedFileModel
import datetime

class Command(BaseCommand):
    help = 'Deletes all overdue files'

    def handle(self, *args, **options):
        files = UploadedFileModel.objects.all()
        overdue = filter(
            lambda f: f.upload_time + datetime.timedelta(days=f.deadline+1) < datetime.date.today(), 
            files
            )
        
        for over in overdue:
            over.delete()

        self.stdout.write(self.style.SUCCESS('Overdue files successfully deleted'))
