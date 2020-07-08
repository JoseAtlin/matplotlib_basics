import csv
import random
import time

x_value = 0
total_1 = 0
total_2 = 0

fieldnames = ["x_value", "total_1", "total_2"]


with open('data_mat9.csv', 'w') as csv_file:
    csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    csv_writer.writeheader()

while 1:
    with open('data_mat9.csv', 'a') as csv_file:
        csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        info = {
            "x_value": x_value,
            "total_1": total_1,
            "total_2": total_2
        }

        csv_writer.writerow(info)
        print(x_value, total_1, total_2)

        x_value += 1
        total_1 = total_1 + random.randint(-5, 8)
        total_2 = total_2 + random.randint(-5, 6)

    time.sleep(1)
