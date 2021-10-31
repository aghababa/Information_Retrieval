import math
import numpy as np


aDCG = np.zeros(2)

aDCG[0] = 1+ 2/math.log(3,2)+ 3/math.log(4,2)+0/math.log(5,2)+0/math.log(6,2)+ 0.5/math.log(7,2) + 0/math.log(8,2) + 1.75/math.log(9,2)
aDCG[1] = 1+ 2/math.log(3,2)+ 2.5/math.log(4,2)+0/math.log(5,2)+0/math.log(6,2)+ 0.25/math.log(7,2) + 0/math.log(8,2) + 2.5/math.log(9,2)

print("DCG:", np.round(aDCG, decimals=4))

aiDCG = 4+ 2.5/math.log(3,2)+ 1/math.log(4,2)+ 0.5/math.log(5,2)+ 0.25/math.log(6,2)

print("alpha-iDCG:", np.round(aiDCG, decimals=4))

print("alpha-nDCG = DCG/iDCG = ", np.round(aDCG/aiDCG, decimals=4))
print("**************************************")
print()


DCG = np.zeros(2)

DCG[0] = 1+ 2/math.log(3,2)+ 3/math.log(4,2)+ 0/math.log(5,2)+ 0/math.log(6,2)+ 1/math.log(7,2) + 0/math.log(8,2) + 4/math.log(9,2)
DCG[1] = 1+ 2/math.log(3,2)+ 4/math.log(4,2)+ 0/math.log(5,2)+ 0/math.log(6,2)+ 1/math.log(7,2) + 0/math.log(8,2) + 3/math.log(9,2)

print("DCG:", np.round(DCG, decimals=4))

iDCG = 4+ 3/math.log(3,2)+ 2/math.log(4,2)+ 1/math.log(5,2)+ 1/math.log(6,2)

print("iDCG:", np.round(iDCG, decimals=4))

print("nDCG = DCG/iDCG = ", np.round(DCG/iDCG, decimals=4))
print("**************************************")
print()




