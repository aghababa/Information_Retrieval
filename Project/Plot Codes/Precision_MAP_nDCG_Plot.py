from matplotlib import pyplot as plt



fig = plt.figure(figsize = (12, 5))
fig.patch.set_facecolor('whitesmoke') 
plt.rc('axes',edgecolor='whitesmoke')
#plt.axis('off')

plt.subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=0.2, hspace=None)

# First plot
fig1 = plt.subplot(1, 2, 1) 
plt.plot([5,10,20], [0.8781, 0.9143, 0.9576], 'blue', label='binary') 
plt.plot([5,10,20], [0.9314, 0.9343, 0.9700], 'tab:orange', label='frequency')
fig1.set(xlabel='k', ylabel='Precision')
plt.legend()

# Second plot
fig2 = plt.subplot(1, 2, 2) 
plt.plot([0.002,0.005,0.01], [0.8634, 0.8775, 0.9171], 'blue', label='binary')
plt.plot([0.002,0.005,0.01], [0.9914, 0.9603, 0.9056], 'tab:orange', label='frequency')
fig2.set(xlabel='r', ylabel='Precision')
plt.legend()

plt.savefig('/Users/hasan/Desktop/Precision.png', bbox_inches='tight', dpi=200)
plt.show()



fig = plt.figure(figsize = (12, 5))
fig.patch.set_facecolor('whitesmoke') 
plt.rc('axes',edgecolor='whitesmoke')

plt.subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=0.2, hspace=None)

# First plot
fig1 = plt.subplot(1, 2, 1) 
plt.plot([5,10,20], [0.8929, 0.8996, 0.9240], 'blue', label='binary') 
plt.plot([5,10,20], [0.8061, 0.7228, 0.7274], 'tab:orange', label='frequency')
fig1.set(xlabel='k', ylabel='MAP')
plt.legend()

# Second plot
fig2 = plt.subplot(1, 2, 2) 
plt.plot([0.002,0.005,0.01], [0.9579, 0.9496, 0.9530], 'blue', label='binary')
plt.plot([0.002,0.005,0.01], [0.9914, 0.9603, 0.8914], 'tab:orange', label='frequency')
fig2.set(xlabel='r', ylabel='MAP')
plt.legend()

plt.savefig('/Users/hasan/Desktop/MAP.png', bbox_inches='tight', dpi=200)
plt.show()




fig = plt.figure(figsize = (12, 5))
fig.patch.set_facecolor('whitesmoke')
plt.rc('axes',edgecolor='whitesmoke')

plt.subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=0.2, hspace=None)

# First plot
# nDCG@5
fig1 = plt.subplot(1, 2, 1) 
plt.plot([5,10,20], [0.9400, 0.7902, 0.5907], 'blue', label="nDCG@5") 
plt.plot([5,10,20], [0.9809, 0.8210, 0.6024], 'tab:orange', label="nDCG@5")
# nDCG@10
plt.plot([5,10,20], [0.9646, 0.9588, 0.8210], color='blue', linestyle='dashed', label="nDCG@10") 
plt.plot([5,10,20], [0.9942, 0.9856, 0.8298], 'tab:orange', linestyle='dashed', label="nDCG@10")
fig1.set(xlabel='k (Binary: blue, Frequency: orange)', ylabel='nDCG')
plt.legend()

# Second plot
fig2 = plt.subplot(1, 2, 2) 
plt.plot([0.002,0.005,0.01], [0.7491, 0.8955, 0.9400], color='blue', label="nDCG@5")
plt.plot([0.002,0.005,0.01], [0.5175, 0.5393, 0.6260], 'tab:orange', label="nDCG@5")
plt.plot([0.002,0.005,0.01], [0.6313, 0.8895, 0.9588], 'blue', linestyle='dashed', label="nDCG@10")
plt.plot([0.002,0.005,0.01], [0.3599, 0.3792, 0.4737], 'tab:orange', linestyle='dashed', label="nDCG@10")
fig2.set(xlabel='r (Binary: blue, Frequency: orange)', ylabel='nDCG')
plt.legend()

plt.savefig('/Users/hasan/Desktop/nDCG.png', bbox_inches='tight', dpi=200)
plt.show()


# Geolife


fig = plt.figure(figsize = (12, 5))
fig.patch.set_facecolor('whitesmoke') 
plt.rc('axes',edgecolor='whitesmoke')

plt.subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=0.2, hspace=None)

# First plot
fig1 = plt.subplot(1, 2, 1) 
plt.plot([5,10,20], [0.8676, 0.8921, 0.9074], 'blue', label='binary') 
plt.plot([5,10,20], [0.9480, 0.9590, 0.9653], 'tab:orange', label='frequency')
fig1.set(xlabel='k', ylabel='Precision')
plt.legend()

# Second plot
fig2 = plt.subplot(1, 2, 2) 
plt.plot([0.001,0.005,0.01], [0.9275, 0.8896, 0.8883], 'blue', label='binary')
plt.plot([0.001,0.005,0.01], [0.9990, 0.9894, 0.9765], 'tab:orange', label='frequency')
fig2.set(xlabel='r', ylabel='Precision')
plt.legend()

plt.savefig('/Users/hasan/Desktop/Precision-Geolife.png', bbox_inches='tight', dpi=200)
plt.show()



fig = plt.figure(figsize = (12, 5))
fig.patch.set_facecolor('whitesmoke') 
plt.rc('axes',edgecolor='whitesmoke')

plt.subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=0.2, hspace=None)

# First plot
fig1 = plt.subplot(1, 2, 1) 
plt.plot([5,10,20], [0.8632, 0.8751, 0.8904], 'blue', label='binary') 
plt.plot([5,10,20], [0.9597, 0.9577, 0.9604], 'tab:orange', label='frequency')
fig1.set(xlabel='k', ylabel='MAP')
plt.legend()

# Second plot
fig2 = plt.subplot(1, 2, 2) 
plt.plot([0.001,0.005,0.01], [0.8116, 0.2025, 0.0376], 'blue', label='binary')
plt.plot([0.001,0.005,0.01], [0.9990, 0.9973, 0.9582], 'tab:orange', label='frequency')
fig2.set(xlabel='r', ylabel='MAP')
plt.legend()

plt.savefig('/Users/hasan/Desktop/MAP-Geolife.png', bbox_inches='tight', dpi=200)
plt.show()



fig = plt.figure(figsize = (12, 5))
fig.patch.set_facecolor('whitesmoke')
plt.rc('axes',edgecolor='whitesmoke')

plt.subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=0.2, hspace=None)

# First plot
# nDCG@5
fig1 = plt.subplot(1, 2, 1) 
plt.plot([5,10,20], [0.9182, 0.7822, 0.5823], 'blue', label="nDCG@5") 
plt.plot([5,10,20], [0.9443, 0.9394, 0.7989], 'tab:orange', label="nDCG@5")
# nDCG@10
plt.plot([5,10,20], [0.9822, 0.8233, 0.6029], color='blue', linestyle='dashed', label="nDCG@10") 
plt.plot([5,10,20], [0.9930, 0.9886, 0.8330], 'tab:orange', linestyle='dashed', label="nDCG@10")
fig1.set(xlabel='k (Binary: blue, Frequency: orange)', ylabel='nDCG')
plt.legend()

# Second plot
fig2 = plt.subplot(1, 2, 2) 
plt.plot([0.001,0.005,0.01], [0.7260, 0.8893, 0.9182], color='blue', label="nDCG@5")
plt.plot([0.001,0.005,0.01], [0.4906, 0.5291, 0.5735], 'tab:orange', label="nDCG@5")
plt.plot([0.001,0.005,0.01], [0.6559, 0.8952, 0.9390], 'blue', linestyle='dashed', label="nDCG@10")
plt.plot([0.001,0.005,0.01], [0.3367, 0.3748, 0.4276], 'tab:orange', linestyle='dashed', label="nDCG@10")
fig2.set(xlabel='r (Binary: blue, Frequency: orange)', ylabel='nDCG')
plt.legend()

plt.savefig('/Users/hasan/Desktop/nDCG-Geolife.png', bbox_inches='tight', dpi=200)
plt.show()


# Grid plot


plt.plot([0.8,2.2,3.1,3.8,4.5, 1.5], [0.7,2.5,1.3,3.2,2.4, 3.4])
plt.xlim(0,5)
plt.ylim(0,5)
plt.grid(b=True)
plt.savefig('/Users/hasan/Desktop/grd.png', bbox_inches='tight', dpi=200)
plt.show()

