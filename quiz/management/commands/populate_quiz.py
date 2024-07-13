from django.core.management.base import BaseCommand
from quiz.models import Area, Question, Option

class Command(BaseCommand):
    help = 'Popula o banco de dados com áreas, perguntas e opções de resposta para o quiz vocacional.'

    def handle(self, *args, **kwargs):
        areas_data = [
            {'name': 'Ciências Exatas e da Terra'},
            {'name': 'Ciências Biológicas'},
            {'name': 'Engenharias'},
            {'name': 'Ciências da Saúde'},
            {'name': 'Ciências Humanas'},
            {'name': 'Ciências Sociais Aplicadas'},
            {'name': 'Linguística, Letras e Artes'},
        ]

        questions_data = [
            {
                'text': 'Qual matéria você mais gosta na escola?',
                'options': [
                    {'text': 'Matemática', 'area': 'Ciências Exatas e da Terra'},
                    {'text': 'Biologia', 'area': 'Ciências Biológicas'},
                    {'text': 'Física', 'area': 'Engenharias'},
                    {'text': 'Química', 'area': 'Ciências da Saúde'},
                    {'text': 'História', 'area': 'Ciências Humanas'},
                    {'text': 'Geografia', 'area': 'Ciências Sociais Aplicadas'},
                    {'text': 'Português', 'area': 'Linguística, Letras e Artes'},
                ]
            },
            {
                'text': 'Qual atividade extracurricular você prefere?',
                'options': [
                    {'text': 'Clube de Matemática', 'area': 'Ciências Exatas e da Terra'},
                    {'text': 'Clube de Ciências', 'area': 'Ciências Biológicas'},
                    {'text': 'Feiras de Engenharia', 'area': 'Engenharias'},
                    {'text': 'Voluntariado em Saúde', 'area': 'Ciências da Saúde'},
                    {'text': 'Debates e Palestras', 'area': 'Ciências Humanas'},
                    {'text': 'Modelos da ONU', 'area': 'Ciências Sociais Aplicadas'},
                    {'text': 'Clube de Leitura', 'area': 'Linguística, Letras e Artes'},
                ]
            },
            {
                'text': 'Qual carreira você se imagina seguindo?',
                'options': [
                    {'text': 'Pesquisador em Física', 'area': 'Ciências Exatas e da Terra'},
                    {'text': 'Biólogo', 'area': 'Ciências Biológicas'},
                    {'text': 'Engenheiro Civil', 'area': 'Engenharias'},
                    {'text': 'Médico', 'area': 'Ciências da Saúde'},
                    {'text': 'Professor de História', 'area': 'Ciências Humanas'},
                    {'text': 'Economista', 'area': 'Ciências Sociais Aplicadas'},
                    {'text': 'Escritor', 'area': 'Linguística, Letras e Artes'},
                ]
            },
            {
                'text': 'Qual tipo de livro você prefere ler?',
                'options': [
                    {'text': 'Livros de Matemática', 'area': 'Ciências Exatas e da Terra'},
                    {'text': 'Livros de Biologia', 'area': 'Ciências Biológicas'},
                    {'text': 'Livros de Física', 'area': 'Engenharias'},
                    {'text': 'Livros de Química', 'area': 'Ciências da Saúde'},
                    {'text': 'Livros de História', 'area': 'Ciências Humanas'},
                    {'text': 'Livros de Geografia', 'area': 'Ciências Sociais Aplicadas'},
                    {'text': 'Romances e Ficção', 'area': 'Linguística, Letras e Artes'},
                ]
            },
            {
                'text': 'Qual tipo de filme você mais gosta?',
                'options': [
                    {'text': 'Ficção Científica', 'area': 'Ciências Exatas e da Terra'},
                    {'text': 'Documentários sobre Natureza', 'area': 'Ciências Biológicas'},
                    {'text': 'Filmes de Engenharia e Tecnologia', 'area': 'Engenharias'},
                    {'text': 'Filmes Médicos', 'area': 'Ciências da Saúde'},
                    {'text': 'Filmes Históricos', 'area': 'Ciências Humanas'},
                    {'text': 'Documentários sobre Sociedade', 'area': 'Ciências Sociais Aplicadas'},
                    {'text': 'Dramas e Clássicos', 'area': 'Linguística, Letras e Artes'},
                ]
            },
            {
                'text': 'Qual é o seu hobby favorito?',
                'options': [
                    {'text': 'Resolver Problemas de Matemática', 'area': 'Ciências Exatas e da Terra'},
                    {'text': 'Explorar a Natureza', 'area': 'Ciências Biológicas'},
                    {'text': 'Construir e Consertar Coisas', 'area': 'Engenharias'},
                    {'text': 'Ajudar Pessoas', 'area': 'Ciências da Saúde'},
                    {'text': 'Ler sobre História', 'area': 'Ciências Humanas'},
                    {'text': 'Estudar Mapas', 'area': 'Ciências Sociais Aplicadas'},
                    {'text': 'Escrever e Ler Livros', 'area': 'Linguística, Letras e Artes'},
                ]
            },
            {
                'text': 'O que mais lhe atrai em uma carreira?',
                'options': [
                    {'text': 'Resolver Problemas Complexos', 'area': 'Ciências Exatas e da Terra'},
                    {'text': 'Entender a Vida e os Organismos', 'area': 'Ciências Biológicas'},
                    {'text': 'Criar e Inovar', 'area': 'Engenharias'},
                    {'text': 'Cuidar da Saúde das Pessoas', 'area': 'Ciências da Saúde'},
                    {'text': 'Ensinar e Transmitir Conhecimento', 'area': 'Ciências Humanas'},
                    {'text': 'Analisar o Funcionamento da Sociedade', 'area': 'Ciências Sociais Aplicadas'},
                    {'text': 'Comunicar Ideias', 'area': 'Linguística, Letras e Artes'},
                ]
            }
        ]

        # Criar áreas
        for area_data in areas_data:
            area, created = Area.objects.get_or_create(name=area_data['name'])
            if created:
                self.stdout.write(self.style.SUCCESS(f'Área "{area.name}" criada com sucesso.'))

        # Criar perguntas e opções
        for question_data in questions_data:
            question = Question.objects.create(text=question_data['text'], area=Area.objects.get(name=question_data['options'][0]['area']))
            for option_data in question_data['options']:
                Option.objects.create(
                    question=question,
                    text=option_data['text'],
                    area=Area.objects.get(name=option_data['area'])
                )
            self.stdout.write(self.style.SUCCESS(f'Pergunta "{question.text}" criada com sucesso.'))

        self.stdout.write(self.style.SUCCESS('População do banco de dados concluída.'))
