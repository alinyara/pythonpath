import numpy as np

cupcakes = np.array([2, 0.75, 2, 1, 0.5])
recipes = np.genfromtxt('recipes.csv', delimiter=',')

print(recipes)
print('number of egs')
eggs = recipes[:, 2]
print(eggs)
n_eggs = recipes[(eggs == 1)]
cookies = recipes[2, :]
double_batch = cupcakes * 2
grocery_list = cookies + double_batch
print(grocery_list)
