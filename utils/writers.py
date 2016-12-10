import csv
from pprint import pformat


def write_to_csv(file: str, data: list, mode: str = 'a'):
    """Write a list of lists to csv."""
    print("**** Writing results to csv")
    csv_file = open(file, mode)
    csv_writer = csv.writer(csv_file, delimiter=',', quotechar='"')

    for item in data:
        csv_writer.writerow(item)

    csv_file.close()


def save_raw_response(response: str, filename: str = "output.txt"):
    with open(filename, "w") as text_file:
        print("{}".format(pformat(response)), file=text_file)
