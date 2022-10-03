import json
import os

from django.core.management.base import BaseCommand

from apps.users.models import User

JSON_PATH = 'fixtures/'
JSON_USERS = 'users'


def load_from_json(file_name):
    with open(os.path.join(JSON_PATH, file_name + '.json'), mode='r', encoding='utf8') as infile:
        return json.load(infile)


class Command(BaseCommand):
    def handle(self, *args, **options):

        admin_is_here = False
        users_num = 0
        users = load_from_json(JSON_USERS)

        User.objects.all().delete()
        for user in users:
            new_user = User.objects.create_user(id=user['pk'],
                                                username=user['fields']['username'],
                                                first_name=user['fields']['first_name'],
                                                last_name=user['fields']['last_name'],
                                                email=user['fields']['email'],
                                                is_superuser=user['fields']['is_superuser'],
                                                is_staff=user['fields']['is_staff'],
                                                is_active=user['fields']['is_active'],
                                                last_login=user['fields']['last_login'],
                                                date_joined=user['fields']['date_joined'],
                                                birthday=user['fields']['birthday'],
                                                note=user['fields']['note'],
                                                banned_at=user['fields']['banned_at'],
                                                )
            if new_user.is_superuser: admin_is_here = True
            new_user.groups.set(user['fields']['groups'])
            new_user.user_permissions.set(user['fields']['user_permissions'])
            new_user.set_password(user['fields']['password'])
            new_user.save()
            users_num += 1
        print(f"Loaded users: {users_num}")

        if admin_is_here:
            print("Super user created.")
