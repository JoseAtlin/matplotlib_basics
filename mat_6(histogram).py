import pandas as pd
from matplotlib import pyplot as plt
from statistics import median

# plt.style.use('fivethirtyeight')

data = pd.read_csv('data_mat6.csv')
ids = data['Responder_id']
ages = data['Age']

bins = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
plt.hist(ages, bins=bins, log=True, edgecolor='black', alpha=.50)

median_age = median(ages)
plt.axvline(median_age, label='Age Median', color='red', linewidth='1', linestyle='--')

plt.legend()
plt.title('Age of Respondents')
plt.xlabel('Ages')
plt.ylabel('No. of Respondents')
plt.tight_layout()
plt.show()
