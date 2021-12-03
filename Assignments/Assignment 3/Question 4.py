import numpy as np
from scipy import linalg as LA

def sim(x, y):
    I_x = np.where(x !=0)[0]
    I_y = np.where(y !=0)[0]
    r_x_bar = np.mean(x[I_x])
    r_y_bar = np.mean(y[I_y])
    I = np.where(x * y != 0)[0]
    x = x[I] - r_x_bar
    y = y[I] - r_y_bar
    similarity = np.dot(x, y)/(LA.norm(x) * LA.norm(y))
    return similarity


Alice = np.array([5, 2, 3, 4, 0, 0])
Bob = np.array([2, 2, 2, 3, 0, 0])
user1 = np.array([3,1,2,3,3,2])
user2 = np.array([3,3,4,3,3,2])
user3 = np.array([3,2,1,5,4,1])
user4 = np.array([2,3,3,4,1,4])


i = 1
for user in [user1, user2, user3, user4]:
    print(f"Similarity of user{i} with Bob: {sim(Bob, user)} \n")
    i += 1


i = 1
for user in [user1, user2, user3, user4]:
    print(f"Similarity of user{i} with Bob: {sim(Alice, user)} \n")
    i += 1


def pred(x, i, kNN_users):
    '''
    x: user
    i: item
    kNN_users: k nearest neighbors to x
    returns: prediction value of recommending item i to the user x
    '''
    a = sum([sim(x, y) * (y[i] - np.mean(y)) for y in kNN_users])
    b = sum([sim(x, y) for y in kNN_users])
    I = np.where(x != 0)[0]
    x = x[I]
    prediction = np.mean(x) + a/b
    return prediction


pred(Alice, i=4, kNN_users=[user1, user3]), pred(Alice, i=5, kNN_users=[user1, user3])

pred(Bob, i=4, kNN_users=[user3, user4]), pred(Bob, i=5, kNN_users=[user3, user4])

for i in range(6):
    print(pred(Alice, i, kNN_users=[user1, user3]))

for i in range(6):
    print(pred(Bob, i, kNN_users=[user3, user4]))


def sim_items(i, j):
    I_i = np.where(i !=0)[0]
    I_j = np.where(j !=0)[0]
    r_i_bar = np.mean(i[I_i])
    r_j_bar = np.mean(j[I_j])
    I = np.where(i * j != 0)[0]
    i = i[I] - r_i_bar
    j = j[I] - r_j_bar
    similarity = np.dot(i, j)/(LA.norm(i) * LA.norm(j))
    return similarity


users = np.array([[3, 1, 2, 3, 3, 2], 
                  [3, 3, 4, 3, 3, 2],
                  [3, 2, 1, 5, 4, 1],
                  [2, 3, 3, 4, 1, 4], 
                  [5, 2, 3, 4, 0, 0], 
                  [2, 2, 2, 3, 0, 0]])
items = users.T
Alice = users[0]
Bob = users[1]
user1 = users[2]
user2 = users[3]
user3 = users[4]
user4 = users[5]

print(items)

for i in range(4):
    print(f"Similarity of item {i} to item 4 with Alice: {sim_items(items[4], items[i])} \n")

for i in range(4):
    print(f"Similarity of item {i} to item 5 with Alice: {sim_items(items[5], items[i])} \n")


def pred_item(i, x, kNN_items):
    '''
    x: user
    i: item
    kNN_items: k nearest neighbors to x
    returns: prediction value of recommending item i to the user x
    '''
    a = sum([sim_items(i, j) * (j[x] - np.mean(j)) for j in kNN_items])
    b = sum([sim_items(i, j) for j in kNN_items])
    I = np.where(i != 0)[0]
    i = i[I]
    prediction = np.mean(i) + a/b
    return prediction


# Alice
pred_item(items[4], 4, kNN_items=[items[0], items[3]]), pred_item(items[5], 4, kNN_items=[items[1], items[2]])

# Bob
pred_item(items[4], 5, kNN_items=[items[0], items[3]]), pred_item(items[5], 5, kNN_items=[items[1], items[2]])

