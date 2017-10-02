import csv


class Gmail:

    def __init__(self):
        pass

    def inbox(self, user):
        user_inbox = []
        if user.logged_in():
            with open('messages.csv', 'r') as file:
                messages = csv.DictReader(file, fieldnames=['message', 'from', 'to', 'timestamp'])
                for message in messages:
                    if message['to'] == user['email']:
                        user_inbox.append(message)

            return user_inbox

        else:
            raise Exception('{} is not logged in.'.format(user.username))
