import csv
import os

from api.instagram import Instagram
from pprint import pprint

def write_to_csv(filepath: str, data: list, mode: str = 'a'):
    print("**** Writing results to csv")
    if not os.path.exists(filepath):
        os.makedirs(filepath)
    csv_file = open(filepath, mode)
    csv_writer = csv.writer(csv_file, delimiter=',', quotechar='"')
    csv_writer.writerow(data)
    csv_file.close()


def main():
    """Main method."""
    #ask for access token
    access_token = input("Access Token: ").strip()
    api = Instagram(access_token)

    pprint(api.get_users_self())


if __name__ == '__main__':
    main()


