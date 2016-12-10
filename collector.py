import os
import getpass
from api.instagram import InstagramAPI
from utils.writers import save_raw_response, write_to_csv
import csv
import random


popular = [
        "224159044",
        "2306025089",
        "1767870805",
        "252710302",
        "1202243774",
        "630616809",
        "2867225022",
        "1671103477",
        "1018216552",
        "8911164",
        "7719696",
        "3428505105",
        "2062601733",
        "233629423",
        "12804395",
        "1339141664",
        "1574083",
        "25025320",
        "1734630055",
        "1496956615",
        "182668366",
        "2630079736",
        "1434659857",
        "610362026"
    ]

def get_user_followers(user_id: str, debug: bool = False):
    """Get followers of a user."""
    username = input("Username:")
    password = getpass.getpass('Password:')

    Instagram = InstagramAPI(username, password)
    Instagram.login()  # login

    users = []
    data = Instagram.getUserFollowers(user_id)

    if debug:
        save_raw_response(data)
    else:
        items = data["users"]
        for item in items:
            user = item
            users.append([user["pk"], user["username"], user["full_name"]])

        write_to_csv(os.path.abspath("results/followers.csv"), users)


def get_username_info(user_id: str = "", debug: bool = False):
    """"Get info about a user."""
    username = input("Username:")
    password = getpass.getpass('Password:')

    Instagram = InstagramAPI(username, password)
    Instagram.login()  # login

    if user_id == "":
        data = Instagram.getSelfUsernameInfo()
    else:
        data = Instagram.getUsernameInfo(user_id)

    if debug:
        save_raw_response(data)
    else:
        user = data["user"]
        user_data = [user["pk"], user["username"], user["full_name"], user["follower_count"], user["following_count"], user["media_count"]]
        write_to_csv(os.path.abspath("results/" + user["pk"] + ".csv"), user_data)


def get_user_feed(user_id: str = "", debug: bool = False):
    """"Get popular posts."""
    username = input("Username:")
    password = getpass.getpass('Password:')

    Instagram = InstagramAPI(username, password)
    Instagram.login()  # login

    posts = []

    if user_id == "":
        data = Instagram.getSelfUserFeed()
    else:
        data = Instagram.getUserFeed(user_id)

    if debug:
        save_raw_response(data)
    else:
        items = data["items"]

        for item in items:
            posts.append([item["id"], item["user"]["pk"], item["user"]["username"], item["taken_at"], item["like_count"], item["comment_count"]])


def get_popular(debug: bool = False):
    """"Get popular posts."""
    username = input("Username:")
    password = getpass.getpass('Password:')

    Instagram = InstagramAPI(username, password)
    Instagram.login()  # login

    users = []
    data = Instagram.getPopularFeed()

    if debug:
        save_raw_response(data)
    else:
        items = data["items"]
        for item in items:
            user = item["user"]
            pk = user["pk"]
            data2 = Instagram.getUsernameInfo(pk)
            user2 = data2["user"]

            users.append([pk, user["username"], user["full_name"], user2["follower_count"], user2["following_count"], user2["media_count"]])

        write_to_csv(os.path.abspath("results/popular.csv"), users)


def construct_dataset():
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

    print("data loaded")

    found_users = []
    while len(found_users) < 50:
        user_info = Instagram.getUsernameInfo(random.choice(users))
        if type(user_info) == bool:
            print("BOOL")
            continue

        user = user_info["user"]
        print("selected user")

        if user["follower_count"] >= 30 and user["following_count"] >= 30 and user["media_count"] >= 60:
            print("user meets criteria")

            found_users.append(
                [user["pk"], user["username"], user["full_name"], user["follower_count"], user["following_count"],
                 user["media_count"]])

            with open('results/dataset.csv', 'a') as csvfile3:
                csv_writer = csv.writer(csvfile3, delimiter=',', quotechar='"')
                csv_writer.writerow(
                    [user["pk"], user["username"], user["full_name"], user["follower_count"], user["following_count"],
                     user["media_count"]])
        else:
            print("user does not meet criteria")


def main():
    """Main method."""




if __name__ == '__main__':
    main()


