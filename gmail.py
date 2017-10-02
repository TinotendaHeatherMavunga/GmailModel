import smtplib
import csv
import datetime


class Gmail:
<<<<<<< HEAD
    pass


    # viewmessage: username, message and timestamp
    def viewmessage(username,message,timestamp):
    	return username + me
=======

    def __init__(self):
        self.user_inbox = []
        pass

    def send_email(self, to_email, msg, subject, user):
        to_address = to_email
        subject = subject
        msg = 'Subject: {}\n\n{}'.format(subject, msg)

        try:
            with open('messages.csv', 'a') as file:
                messages = csv.DictWriter(file, fieldnames=['from', 'to', 'message', 'timestamp'])
                messages.writerow({'from': user.email, 'to': to_address, 'message': msg, 'timestamp': datetime.datetime.now() })

                print('Message sent successfully to {}'.format(to_email))

        except Exception as e:
            print('Sorry email was not sent, Try again', e)

    def compose_email(self, user):
        subject = input('Please enter subject: ')
        message = input("Compose new message here: ")
        to = input('Enter email address: ')
        self.send_email(to, message, subject, user)

    def inbox(self, user):
        if user.logged_in():
            with open('messages.csv', 'r') as file:
                messages = csv.DictReader(file, fieldnames=['message', 'from', 'to', 'timestamp'])
                for message in messages:
                    if message['to'] == user['email']:
                        self.user_inbox.append(message)

            return self.user_inbox

        else:
            raise Exception('{} is not logged in.'.format(user.username))
>>>>>>> 79f39caac02056169b943e48a8685767bbdd28f8
