from matplotlib import pyplot as plt
from statistics import median
import pandas as pd

# plt.style.use('fivethirtyeight')

data = pd.read_csv('data_mat5,10.csv')
ages = data['Age']
dev_salaries = data['All_Devs']
py_salaries = data['Python']
js_salaries = data['JavaScript']

# median = median(dev_salaries)
# plt.plot(ages, dev_salaries, label='All Devs')
plt.plot(ages, py_salaries, linestyle='--', label='Py Devs')
plt.plot(ages, js_salaries, linestyle='--', label='JS Devs')


plt.fill_between(ages, py_salaries, js_salaries, where=(py_salaries > js_salaries), interpolate=True,
                 alpha=.25, label='Python prevails')
plt.fill_between(ages, py_salaries, js_salaries, where=(py_salaries <= js_salaries), interpolate=True,
                 alpha=.25, label='JS prevails')


plt.legend()
plt.title('Median Salary (USD) by Age')
plt.xlabel('Ages')
plt.ylabel('Median Salaries (USD)')
plt.tight_layout()
plt.show()
