# Importing Matplotlib
# Basic Plot

import matplotlib.pyplot as plt
x = [1,2,3,4,5]
y = [12,23,34,56,76]

plt.plot(x,y)
plt.title('Line Plot')
plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.show()

plt.scatter(x,y)
plt.title('Scatter Plot')
plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.show()

categories = ['A', 'B', 'C', 'D']
values = [4,7,1,8]
plt.bar(categories, values)
plt.title('Bar Plot')
plt.xlabel('Categories')
plt.ylabel('Values')
plt.show()

data = [1,2,2,3,3,3,4,4,4,4]
plt.hist(data, bins = 4)
plt.title('Histogram')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.show()

x = [1,2,3,4,5]
y = [2, 3 ,5, 6, 11]
plt.plot(x,y, label = "Prime Numbers")
plt.title('Line Plot with Grid and Legend')
plt.xlabel('X axis')
plt.ylabel('Y axis')
plt.legend()
plt.show()

plt.subplot(x,y)
plt.title('Plot 1')
plt.subplot(1,2,2)
plt.bar(categories, values)
plt.title('Plot 2')
plt.show()

import seaborn as sns
sns.lineplot(x=x, y=y)
plt.title('Line Plot with Seaborn')
plt.show()

sns.scatterplot(x=x, y=y)
plt.title('Scatter Plot with Seaborn')
plt.show()

sns.barplot(x=categories, y=values)
plt.title('Bar Plot with Seaborn')
plt.show()

sns.histplot(data, bins=4, kde=True)
plt.title('Histogram and KDE Plot')
plt.show()

tips = sns.load_data('tips')
sns.boxplot(x='day', y='total_bill', data=tips)
plt.title('BoxPlot')
plt.show()

tips = sns.load_dataset('tips')
sns.vioinplot(x='day', y='total_bill', data='tips')
plt.title('Violin Plot')
plt.show()

tips = sns.load_dataset('tips')
sns.pairplot(tips)
plt.title('PairPlot')
plt.show()




















