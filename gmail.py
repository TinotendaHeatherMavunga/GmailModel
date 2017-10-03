import smtplib
import os
import csv
import datetime


class Gmail:

    user_inbox = []

    def __init__(self):
        print('############################')
        print('#######    Gmail   #########')
        print('############################')

    def send_email(cls, to_email, msg, subject, user):
        to_address = to_email
        subject = subject
        msg = '{}'.format(subject, msg)

        try:
            has_header = False
            with open('messages.csv', 'r') as f:
                for line in f:
                    if len(line)>=1:
                        has_header = True
                        break
                    else:
                        pass
            with open('messages.csv', 'a') as file:
                messages = csv.DictWriter(file, fieldnames=['from', 'to', 'message', 'subject', 'timestamp'])
                if not has_header:
                    messages.writeheader()
                messages.writerow({'from': user.email_address, 'to': to_address, 'subject': subject, 'message': msg, 'timestamp': datetime.datetime.now() })

                print('Message sent successfully to {}'.format(to_email))

        except Exception as e:
            print('Sorry email was not sent, Try again.', 'Error Message: ',e)

    def compose_email(cls, user):
        subject = input('Please enter subject: ')
        message = input("Compose new message here: ")
        to = input('Enter email address: ')
        cls.send_email(to, message, subject, user)

    def inbox(cls, user):
        if user.logged_in:
            with open('messages.csv', 'r') as file:
                messages = csv.DictReader(file, fieldnames=['from', 'to', 'message', 'subject', 'timestamp'])
                for message in messages:
                    if message['to'] == user.email_address:
                        cls.user_inbox.append(message)

            return cls.user_inbox

        else:
            raise Exception('{} is not logged in.'.format(user.username))

    def view_mesasge(cls,index,inbox):
        return inbox[index]
