import csv
import os
import bcrypt


class Account:

    def __init__(self, firstname, lastname, gender, username, password):
        with open("accounts.csv", "r") as file_handler:
            reader = csv.DictReader(file_handler)
            for user in reader:
                if user["username"] == username:
                    try:
                        return ValueError
                    except ValueError:
                        return "Sorry, that username is taken!"
            else:
                hashed = bcrypt.hashpw(
                    password.encode("utf-8"), bcrypt.gensalt())
                self.firstname = firstname
                self.lastname = lastname
                self.gender = gender
                self.username = username
                self.password = hashed

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
