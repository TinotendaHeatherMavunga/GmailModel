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
<<<<<<< HEAD
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
    
    #testing signing
    def signin(self):
        with open ('accounts.csv','r') as file_handler:
            checker = csv.DictReader(file_handler)
            loguser = input('Enter Username: ')
            logpass = input('Enter password: ')
            logpass = bcrypt.hashpw(
                    logpass.encode("utf-8"), bcrypt.gensalt())


            for user in checker:
                if loguser == user['username']:
                    print("Username correct")

                else:
                    print("Username incorrect")
                    break


a = Account('Eyram','Amedzor','M','eyramm','kofi1234')

a.signin()
=======

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
            hashed = bcrypt.hashpw(
                password.encode("utf-8"), bcrypt.gensalt())
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
>>>>>>> 79f39caac02056169b943e48a8685767bbdd28f8
