import csv
import os
import bcrypt


class Account:
    # Account constructor method - instantiates a new Account object

    def __init__(self, firstname, lastname, gender, username, password):

        # reads accounts.csv to check if username is available
        with open("accounts.csv", "r") as file_handler:
            reader = csv.DictReader(file_handler)
            user_available = True
            for user in reader:
                if user["username"] == username:
                    user_available = False
                    try:
                        raise ValueError
                    except ValueError:
                        print("Sorry, that username is taken!")

            # if username is available
            if user_available:
                hashed = bcrypt.hashpw(
                    password.encode("utf-8"), bcrypt.gensalt())
                self.firstname = firstname
                self.lastname = lastname
                self.gender = gender
                self.username = username
                self.password = hashed

                # writes the new object to accounts.csv
                # This should be broken out into its own method, please
                with open("accounts.csv", "a") as file_handler:
                    fieldnames = [
                        "firstname",
                        "lastname",
                        "gender",
                        "username",
                        "password"]
                    writer = csv.DictWriter(
                        file_handler, fieldnames=fieldnames)
                    if os.path.getsize("accounts.csv") == 0:
                        writer.writeheader()
                    writer.writerow(self.__dict__)

#
# new_account = CreateAccount() # first name, last name, email, username, password, gender, logged_in=False
# existing_account = Account(username, password) # check if account exists, if it exists, do existing_account.login()
# existing_account.logged_in
# self.logged_in = self.login(username, password)
# if self.logged_in:
#     self.account = get_user()
#     self.firstname = self.account['firstname']
#     self.lastname
#     self.email
#     self.username
#     self.password
#     self.gender
# gmail = Gmail()
# if existing_account.logged_in:
#     gmail.inbox(existing_account)