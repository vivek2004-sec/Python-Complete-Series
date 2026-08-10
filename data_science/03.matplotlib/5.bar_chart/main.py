import matplotlib.pyplot as plt
import numpy as np

# Bar Chart = compare categories of data by representing each category with bar.

# categories = np.array(['Grains', 'Fruits', 'Vegetables', 'Protein', 'Dairy ', 'Sweets'])
# values = np.array([4, 3, 2, 4.5, 3.5, 4])


# plt.title("Food consumption")
# plt.xlabel('Food', fontsize=15)
# plt.ylabel('Consumption', fontsize=15)
# # plt.bar(categories, values)
# # plt.barh(categories, values)
# plt.show()

categories = np.array(['Freshmen', 'Sophomores', 'Juniors', 'Seniors'])
values = np.array([300, 230, 450, 220])
colors = np.array(['red', 'yellow', 'green', 'blue'])
plt.pie( values, labels=categories, 
        autopct='%1.1f%%', 
        colors=colors)
plt.show()