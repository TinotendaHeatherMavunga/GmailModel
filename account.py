import csv
import os
import bcrypt


class Account:
    # Account constructor method - instantiates a new Account object

    def __init__(self):

        # Take in user input for the Account fields
        print("Welcome to GMail, Please enter the following details")
        firstname = input("Enter first name: ")
        lastname = input("Enter last name: ")
        phone = input("Enter your phone number: ")
        recovery_email = input("Enter recovery email: ")
        gender = input("Enter gender: ")

        while True:
            username = input("Enter your username: ")
            password = input("Enter your password: ")
            confirm_password = input("Re-Enter your password: ")
            user_available = True

            # check if passwords match
            if password == confirm_password:

                # check accounts.csv if username is available
                with open("accounts.csv", "r") as data_file:
                    user_data = csv.DictReader(data_file)
                    for user in user_data:
                        if user["username"] == username:
                            user_available = False
                            try:
                                raise ValueError
                            except ValueError:
                                print("Sorry, the username already exists")
                                break
                if user_available:
                    break
            else:
                print("Sorry, passwords do not match, try again!")
                continue

        # if username is available and passwords match
        if user_available:
            hashed = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())
            self.firstname = firstname
            self.lastname = lastname
            self.phone = phone
            self.recovery_email = recovery_email
            self.gender = gender
            self.username = username
            self.password = hashed
            self.logged_in = False
            self.email_address = "{}@gmail.com".format(self.username)
        self.write_account()

    # writes the new object to accounts.csv
    def write_account(self):
        with open("accounts.csv", "a") as file_handler:
            fieldnames = [
                "firstname",
                "lastname",
                "phone",
                "recovery_email",
                "gender",
                "username",
                "password",
                "logged_in",
                "email_address"]
            writer = csv.DictWriter(
                file_handler, fieldnames=fieldnames)
            if os.path.getsize("accounts.csv") == 0:
                writer.writeheader()
            writer.writerow(self.__dict__)

    @classmethod
    def login(cls):
        with open("accounts.csv", "r")as file:
            user_data = csv.DictReader(file)

            username = input("Enter username: ")
            password = input("Enter password: ")
            password_match = False
            user_found = False
            for user in user_data:
                if user["username"] == username:
                    user_found = True
                    user["password"] = user["password"][2:-1].encode("utf-8")
                    print(user)
                    if bcrypt.checkpw(password.encode(
                            "utf-8"), user["password"]):
                        password_match = True
                        existing_user = UserAccount(**user)
                        existing_user.logged_in = True
                        return existing_user
            if not user_found:
                print("User not found!!")
            else:
                if not password_match:
                    print("Sorry Passwords do not match!!")

# UserAccount class creates a user object from accounts.csv iff
# Account.login succeeds


class UserAccount:

    def __init__(self, firstname, lastname, phone, recovery_email,
                 gender, username, password, logged_in, email_address):
        self.firstname = firstname
        self.lastname = lastname
        self.phone = phone
        self.recovery_email = recovery_email
        self.gender = gender
        self.username = username
        self.password = password
        self.logged_in = False
        self.email_address = email_address
