from django.core.management.base import BaseCommand
from quiz.models import Area, Question, Option, Result

class Command(BaseCommand):
    help = 'Reseta os dados do quiz vocacional.'

    def handle(self, *args, **kwargs):
        self.stdout.write('Resetando dados do quiz...')
        Result.objects.all().delete()
        Option.objects.all().delete()
        Question.objects.all().delete()
        Area.objects.all().delete()
        self.stdout.write(self.style.SUCCESS('Dados do quiz resetados com sucesso.'))
