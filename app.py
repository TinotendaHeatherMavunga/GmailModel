from account import Account
from gmail import Gmail


gmail = Gmail()

while True:
    choice = input('1. Sign up\n2. Login\n')
    if choice == '1':
        new_account = Account()
    elif choice == '2':
        user_account = Account.login()
        if user_account != None:
            while True:
                choice2 = input('1. Inbox\n2.Send Email\n')
                if choice2 == '1':
                    inbx = gmail.inbox(user_account)
                    print(inbx)
                    choice3 = input('Enter the index of message to view (max {}) / -1 to go back: '.format(len(inbx)-1))
                    if int(choice3) == -1:
                        pass
                    else:
                        print(inbx[int(choice3)])
                elif choice2 == '2':
                    #to_email, msg, subject, user
                    t = input('To: ')
                    s = input('Subject: ')
                    m = input('Message: ')
                    gmail.send_email(t, m, s, user_account)

