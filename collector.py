import csv
import os
import getpass
from api.instagram import InstagramAPI
from pprint import pprint


def write_to_csv(file: str, data: list, mode: str = 'a'):
    """Write a list of lists to csv."""
    print("**** Writing results to csv")
    csv_file = open(file, mode)
    csv_writer = csv.writer(csv_file, delimiter=',', quotechar='"')

    for item in data:
        csv_writer.writerow(item)

    csv_file.close()


def getPopular():
    """"Get popular posts."""

    username = input("Username:")
    password = getpass.getpass('Password:')

    Instagram = InstagramAPI(username, password)
    Instagram.login()  # login

    users = []
    data = Instagram.getPopularFeed()
    items = data["items"]
    for item in items:
        user = item["user"]
        users.append([user["pk"], user["username"], user["full_name"]])

    write_to_csv(os.path.abspath("results/popular.csv"), users)


def main():
    """Main method."""
    getPopular()

if __name__ == '__main__':
    main()


