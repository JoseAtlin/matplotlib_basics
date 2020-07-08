from matplotlib import pyplot as plt
import numpy as np

# plt.xkcd()                                    #hand written style
# plt.style.use('seaborn')                      #matplotlib has bulitin styles. To check them run -> print(plt.style.available)

ages_x = [20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39]                               #x_axis values
# x_indexes = np.arange(len(ages_x))
# width = 0.25


py_dev_y = [20000, 24744, 30500, 37732, 41247, 45372, 48876, 53850, 57287, 63016, 65998, 70003, 70000, 71496, 75370,    #y_axis values, but here we have 3 plots to represent -> python, javascript, All developers
            83640, 84666, 84392, 78254, 85000]
plt.plot(ages_x, py_dev_y, color='red', linestyle='--', label='Python')                                                 #python values
# plt.bar(x_indexes - width, py_dev_y, width=width, color='red', label='Python')


js_dev_y = [18942, 21780, 25704, 29000, 34372, 37810, 43515, 46823, 49293, 53437, 56373, 62375, 66674, 68745, 68746,    #JS values
            74583, 79000, 78508, 79996, 80403]
plt.plot(ages_x, js_dev_y, color='green', linestyle='--', label='JavaScript')
# plt.bar(x_indexes, js_dev_y, color='green', width=width, label='JavaScript')


dev_y = [18012, 20628, 25206, 30252, 34368, 38496, 42000, 46752, 49320, 53200, 56000, 62316, 64928, 67317, 68748,       #All Dev values
         73752, 77232, 78000, 78508, 79536]
plt.plot(ages_x, dev_y, color='black', linestyle='solid', marker='.', label='All Devs')
# plt.bar(x_indexes + width, dev_y, color='black', width=width, label='All Devs')

# plt.xticks(ticks=x_indexes, labels=ages_x)
plt.title('Median Salary (USD) by Age')                                 #set_title
plt.xlabel('Ages ->')                                                   #set_x_axis_label, y_axis_label
plt.ylabel('Median Salary (USD) ->')                                    
plt.legend()                                                            #to display the data plotted i.e. (print -> label=python, javascript)
plt.grid(True)                                                          #to display grid
plt.tight_layout()                                                      #used to get all the data in the figure (mainly for laptop users since the figure gets some unwanted padding which makes affects the visibility of data)
# plt.savefig('plot.png')                                               #save the plot
plt.show()                                                              #show the figure
