import getpass
from api.instagram import InstagramAPI
import csv
import random


def collect_users():
    username = input("Username:")
    password = getpass.getpass('Password:')

    Instagram = InstagramAPI(username, password)
    Instagram.login()  # login

    users = []
    with open('results/popular.csv', 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='"')
        for row in reader:
            users.append(row[0])

    with open('results/followers.csv', 'r') as csvfile2:
        reader = csv.reader(csvfile2, delimiter=',', quotechar='"')
        for row in reader:
            users.append(row[0])

    already = []
    with open('results/users.csv', 'r') as csvfile0:
        reader = csv.reader(csvfile0, delimiter=',', quotechar='"')
        for row in reader:
            already.append(row[0])

    print("data loaded")

    found_users = []
    while len(found_users) < (100 - len(already)):
        user_info = Instagram.getUsernameInfo(random.choice(users))
        if type(user_info) == bool:
            print("BOOL")
            continue

        user = user_info["user"]

        if user["pk"] in already:
            print("already")
            continue

        print("selected user")

        if user["follower_count"] >= 30 and user["following_count"] >= 30 and user["media_count"] >= 60 and not user["is_private"]:
            print("user meets criteria")

            found_users.append(
                [user["pk"], user["username"], user["full_name"], user["follower_count"], user["following_count"],
                 user["media_count"]])

            with open('results/users.csv', 'a') as csvfile3:
                csv_writer = csv.writer(csvfile3, delimiter=',', quotechar='"')
                csv_writer.writerow(
                    [user["pk"], user["username"], user["full_name"], user["follower_count"], user["following_count"],
                     user["media_count"]])
        else:
            print("user does not meet criteria")


def find_duplicate_users():
    already = []
    duplicates_found = False
    with open('results/users.csv', 'r') as csvfile0:
        reader = csv.reader(csvfile0, delimiter=',', quotechar='"')
        for row in reader:
            if row[0] in already:
                duplicates_found = True
                print(row[0])
            already.append(row[0])

    if not duplicates_found:
        print('no duplicates')
        

def collect_posts():
    username = input("Username:")
    password = getpass.getpass('Password:')

    Instagram = InstagramAPI(username, password)
    Instagram.login()  # login

    users = []
    with open('results/users.csv', 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='"')
        for row in reader:
            users.append(row[0])

    already = set()
    with open('results/posts.csv', 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='"')
        for row in reader:
            already.add(row[1])

    print("data loaded")

    for u in users:
        if u in already:
            print("already")
            continue

        data = Instagram.getUserFeed(u)

        if type(data) == bool:
            print("BOOL")
            continue

        items = data["items"]
        print("writing to csv")
        for item in items:
            with open('results/posts.csv', 'a') as csvfile2:
                csv_writer = csv.writer(csvfile2, delimiter=',', quotechar='"')
                csv_writer.writerow(
                    [item["id"], item["user"]["pk"], item["user"]["username"], item["taken_at"], item["like_count"],
                     item["comment_count"]]
                )

def main():
    """Main method."""
    #collect_users()
    find_duplicate_users()


if __name__ == '__main__':
    main()


