from django.core.management.base import BaseCommand, CommandError
from useractivity.models import User as Poll


class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def add_arguments(self, parser):
        parser.add_argument('poll_ids', nargs='+', type=int)

        # Named (optional) arguments
        parser.add_argument(
            '--delete',
            action='store_true',
            help='Delete user instead of closing it',
        )

    def handle(self, *args, **options):
        for poll_id in options['poll_ids']:
            try:
                poll = Poll.objects.get(pk=poll_id)
            except Poll.DoesNotExist:
                raise CommandError(
                    'User with  "%s"  id does not exist' % poll_id)

            poll.opened = False
            poll.save()

            self.stdout.write(self.style.SUCCESS(
                'Successfully closed User  %s' % poll.user_name))
            if options['delete']:
                poll.delete()
