from flask import Flask, request
from flask_cors import CORS
import numpy as np 
import pandas as pd
from scipy import linalg as LA
from termcolor import colored 



def dic(a, b):
    return {a:b}
def status(r):
    return r.method, r.get_data()
def decompose(d):
    return d['user_entered_traj'], d['k'], d['r'], d['option']
#.........................................................................

sigma_coeff = 3
reduction_dim = 100 #25
max_limit = 50

x = np.array(pd.read_csv('data/x.csv', header=None))[0]
y = np.array(pd.read_csv('data/y.csv', header=None))[0]
n_x_grids = len(x) - 1
n_y_grids = len(y) - 1

reducedData = np.array(pd.read_csv('data/reducedData_binary.csv', header=None))
Delta_0_sqrt_Pt_multipass = np.array(pd.read_csv('data/Delta_0_sqrt@Pt_multipass.csv', header=None))
Delta_0_sqrt_Pt_binary = np.array(pd.read_csv('data/Delta_0_sqrt@Pt_binary.csv', header=None))
U_e_multipass = np.array(pd.read_csv('data/U_e_multipass.csv', header=None))
U_e_binary = np.array(pd.read_csv('data/U_e_binary.csv', header=None))

print('reducedData.shape=', reducedData.shape)
print('Delta_0_sqrt_Pt_multipass.shape=', Delta_0_sqrt_Pt_multipass.shape)
print('Delta_0_sqrt_Pt_binary.shape=', Delta_0_sqrt_Pt_binary.shape)
print('U_e_multipass.shape=', U_e_multipass.shape)
print('U_e_binary.shape=', U_e_binary.shape)


def vectorizeLineSegment(LineSegment): 
    '''
    LineSegment: of shape (2, 2); coordinates of start and end are given; [[x1, y1], [x2, y2]]
    return: a binary vector of length n_x_grids x n_y_grids, which shows if 
            LineSegment has occured in each grid or not
    '''
    array = np.zeros((n_x_grids, n_y_grids))
    p1, p2 = LineSegment
    slope = (p2-p1)[1]/((p2-p1)[0] + 1e-10)
    i1 = np.where(x - p1[0] < 0)[0][-1]
    i2 = np.where(x - p2[0] < 0)[0][-1]
    xIdxStart = min(i1, i2)
    xIdxEnd = max(i1, i2)

    if xIdxEnd != xIdxStart:
        ''' dealing with start point of lineSegment'''
        if i1 < i2:
            j_start = np.where(y - p1[1] < 0)[0][-1]
            y_val_end = slope * (x[i1+1] - p1[0]) + p1[1]
        else:
            j_start = np.where(y - p2[1] < 0)[0][-1]
            y_val_end = slope * (x[i2+1] - p1[0]) + p1[1]
        j_end = np.where(y - y_val_end < 0)[0][-1]
        array[xIdxStart][np.arange(min(j_start, j_end), max(j_start, j_end)+1)] = 1

        ''' dealing with end point of lineSegment'''
        if i1 < i2:
            j_end = np.where(y - p2[1] < 0)[0][-1]
            y_val_start = slope * (x[i2] - p1[0]) + p1[1]
        else:
            j_end = np.where(y - p1[1] < 0)[0][-1]
            y_val_start = slope * (x[i1] - p1[0]) + p1[1]
        j_start = np.where(y - y_val_start < 0)[0][-1]
        array[xIdxEnd][np.arange(min(j_start, j_end), max(j_start, j_end)+1)] = 1

        ''' dealing with non-endpoints of lineSegment'''
        for i in range(xIdxStart+1, xIdxEnd):
            y_val_start = slope * (x[i] - p1[0]) + p1[1]
            y_val_end = slope * (x[i+1] - p1[0]) + p1[1]
            j_start = np.where(y - y_val_start < 0)[0][-1]
            j_end = np.where(y - y_val_end < 0)[0][-1]
            array[i][np.arange(min(j_start, j_end), max(j_start, j_end)+1)] = 1
    else:
        y_val_start = min(p1[1], p2[1])
        y_val_end = max(p1[1], p2[1])
        j_start = np.where(y - y_val_start < 0)[0][-1]
        j_end = np.where(y - y_val_end < 0)[0][-1]
        array[xIdxStart][np.arange(min(j_start, j_end), max(j_start, j_end)+1)] = 1
    return array.reshape(n_x_grids * n_y_grids)


def vectorizeTrajectory(trajectory, option): # T --> T_tilda
    '''
    trajectory: of shape (m, 2)
    return: a vector of length n_x_grids x n_y_grids, which shows the number 
            of occurences of trajectory in each grid
    '''
    A = [vectorizeLineSegment(trajectory[i:i+2]) for i in range(len(trajectory) - 1)]
    if option == 'multipass':
        return np.sum(A, axis=0)
    elif option == 'binary':
        return np.sign(np.sum(A, axis=0))


def dimReducedQuery(query, option):
    if option == 'multipass':
        projection = Delta_0_sqrt_Pt_multipass
        U_e = U_e_multipass
    elif option == 'binary':
        projection = Delta_0_sqrt_Pt_binary
        U_e = U_e_binary
    T_q_tilda = vectorizeTrajectory(query, option=option) # vectorizedQuery
    T_q_tilda_tilda = projection @ T_q_tilda
    T_q_e_tilda_tilda = U_e.T @ T_q_tilda_tilda
    return T_q_e_tilda_tilda 


def queryRankList(query, reduction_dim, option, max_limit, k=None, r=None): 
    '''
    returns a list; the indices of the trajectories to be retrieved for the query
    '''
    mappedReducedQuery = dimReducedQuery(query, option=option)
    distQueryFromReducedData = LA.norm(reducedData - mappedReducedQuery.reshape(reduction_dim,1), 
                                       axis=0) / (n_x_grids * n_y_grids)
    distQueryFromReducedDataSortedIndices = np.argsort(distQueryFromReducedData)
    if k:
        return distQueryFromReducedDataSortedIndices[:k]
    elif r:
        idx = np.where(distQueryFromReducedData < r)[0]
        return idx[:max_limit].tolist()
    else:
        print(colored("Please specify k or r", "yellow"))
        return




def computation(rec):
    user_entered_traj, k, r, option = decompose(rec)
    user_entered_traj = np.array(user_entered_traj)
    a = queryRankList(user_entered_traj, reduction_dim, option, max_limit, k=k, r=r)
    a = list(map(str, a))
    return a












#.........................................................................
def App(s):
    arg = 'da'
    out = computation(eval(s[1]))
    if s[0] == 'POST':
        return dic(arg, out)
    else:
        return dic(arg, [])
app = Flask(__name__)
CORS(app)
@app.route('/i', methods=['GET', 'POST'])
def application():
    s = status(request)
    return App(s)
if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5050, debug = True)