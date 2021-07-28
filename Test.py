import matplotlib.pyplot as plt
import seaborn
import pandas

tumor_size = [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 70, 75, 80, 85, 90, 95, 100, 105, 110, 115, 150]

malignant = [0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50]

data = pandas.DataFrame(tumor_size, malignant)
seaborn.regplot(x=tumor_size, y=malignant, data=data, scatter_kws={"s": 80})

plt.show()
