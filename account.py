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
