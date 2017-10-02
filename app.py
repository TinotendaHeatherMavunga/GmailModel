from gmail import Gmail
from account import Account


print("#################################")
print("######       Gmail         ######")
print("#################################")

print("\n\n")

choice = input("1. Sign Up \n2. Login \n")
user_account = None
gmail = Gmail()

while True:

	if choice == '1':
		new_account = Account()
		user_account = Account.login()

	elif choice == '2':
		user_account = Account.login()



	if user_account.logged_in:
		print(gmail.inbox(user_account))

		choice2 = input("1. Compose Email \n2. View Message \n")

		if choice2 == '1':
			gmail.compose_email(user_account)