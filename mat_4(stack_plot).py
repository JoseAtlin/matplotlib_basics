from matplotlib import pyplot as plt

plt.style.use("fivethirtyeight")

hour = [1, 2, 3, 4, 5, 6, 7, 8, 9]
dev1 = [8, 6, 5, 5, 4, 2, 1, 1, 0]
dev2 = [0, 1, 2, 2, 2, 4, 4, 4, 4]
dev3 = [0, 1, 1, 1, 2, 2, 3, 3, 4]

labels = ['dev1', 'dev2', 'dev3']
colors = ['#6d904f', '#fc4f30', '#008fd5']

plt.stackplot(hour, dev1, dev2, dev3, labels=labels, colors=colors)

plt.legend(loc=(0.07, 0.05))
plt.title("Hour wise work distribution")
plt.tight_layout()
plt.show()
