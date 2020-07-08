import csv
import pandas as pd
from collections import Counter
from matplotlib import pyplot as plt

plt.style.use("fivethirtyeight")

# csv.register_dialect('mydialect',
#                      delimiter=',',
#                      skipinitialspace=True,
#                      quoting=csv.QUOTE_ALL)

with open('data_mat2.csv', mode='r') as csv_file:                       # row = next(csv_file)
    csv_reader = csv.DictReader(csv_file)                           # print(row['LanguagesWorkedWith'].split(';'))

    lang_count = Counter()
    for row in csv_reader:
        lang_count.update(row['LanguagesWorkedWith'].split(';'))


# data = pd.read_csv('data_mat2.csv')
# ids = data['Responder_id']
# lang_responses = data['LanguagesWorkedWith']
#
# lang_count = Counter()
#
# for response in lang_responses:
#     lang_count.update(response.split(';'))


# languages, popularity = map(list, zip(*lang_count.most_common(15)))
languages = []
popularity = []
for item in lang_count.most_common(15):
    languages.append(item[0])
    popularity.append(item[1])


languages.reverse()
popularity.reverse()

plt.barh(languages, popularity)
plt.title("Most Popular Languages")
plt.xlabel("Number of People Who Use")
plt.ylabel("Programming Languages")
plt.tight_layout()
plt.show()
