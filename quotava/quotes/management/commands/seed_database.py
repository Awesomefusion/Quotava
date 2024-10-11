from django.core.management.base import BaseCommand
from quotes.models import Author, Quote, Category, User


class Command(BaseCommand):
    help = 'Seed the database with initial data'

    def handle(self, *args, **kwargs):
        self.create_users()
        self.create_categories()
        self.create_authors_and_quotes()

        self.stdout.write(self.style.SUCCESS('Database seeded successfully'))

    def create_users(self):
        if User.objects.count() == 0:
            # Create 9 default users
            for i in range(1, 10):
                User.objects.create_user(username=f'user{i}', password='password')

            # Create 1 admin user
            User.objects.create_user(username='admin', password='adminpassword', is_admin=True, is_staff=True,
                                     is_superuser=True)

            self.stdout.write(self.style.SUCCESS('Created 9 default users and 1 admin user'))

    def create_categories(self):
        if Category.objects.count() == 0:
            categories = ['Innovation', 'Technology', 'Leadership', 'Business', 'Future', 'Entrepreneurship']
            for category in categories:
                Category.objects.create(name=category)
            self.stdout.write(self.style.SUCCESS('Created 6 categories'))

    def create_authors_and_quotes(self):
        if Quote.objects.count() == 0:
            # Create authors if they don't exist
            jeff_bezos, created = Author.objects.get_or_create(name='Jeff Bezos')
            elon_musk, created = Author.objects.get_or_create(name='Elon Musk')
            bill_gates, created = Author.objects.get_or_create(name='Bill Gates')
            steve_jobs, created = Author.objects.get_or_create(name='Steve Jobs')
            larry_page, created = Author.objects.get_or_create(name='Larry Page')
            mark_zuckerberg, created = Author.objects.get_or_create(name='Mark Zuckerberg')
            sundar_pichai, created = Author.objects.get_or_create(name='Sundar Pichai')
            tim_berners_lee, created = Author.objects.get_or_create(name='Tim Berners-Lee')

            # Create quotes for Jeff Bezos
            Quote.objects.get_or_create(
                text='If you do build a great experience, customers tell each other about that. Word of mouth is very powerful.',
                author=jeff_bezos,
                user=User.objects.get(username='admin')
            )
            Quote.objects.get_or_create(
                text='Your brand is what other people say about you when you\'re not in the room.',
                author=jeff_bezos,
                user=User.objects.get(username='admin')
            )

            # Create quotes for other prominent tech figures
            quotes = [
                ('When something is important enough, you do it even if the odds are not in your favor.', elon_musk),
                ('Don\'t compare yourself with anyone in this world. If you do so, you are insulting yourself.',
                 bill_gates),
                ('Innovation distinguishes between a leader and a follower.', steve_jobs),
                ('Always deliver more than expected.', larry_page),
                ('The biggest risk is not taking any risk.', mark_zuckerberg),
                ('We will build the devices for what we do online today and future things that haven’t been done yet.',
                 sundar_pichai),
                (
                'The Web as I envisaged it, we have not seen it yet. The future is still so much bigger than the past.',
                tim_berners_lee)
            ]

            for text, author in quotes:
                Quote.objects.get_or_create(
                    text=text,
                    author=author,
                    user=User.objects.get(username=f'user{quotes.index((text, author)) + 1}')
                )

            self.stdout.write(self.style.SUCCESS('Created 10 quotes (2 from Jeff Bezos and 8 from others)'))
