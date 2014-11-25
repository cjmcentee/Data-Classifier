__author__ = 'coltonmcentee'

import random


MESSY_MEAN_X_1 = 350
MESSY_STD_X_1  = 100
MESSY_MEAN_Y_1 = 0
MESSY_STD_Y_1  = 400

MESSY_MEAN_X_2 = 100
MESSY_STD_X_2  = 200
MESSY_MEAN_Y_2 = 1000
MESSY_STD_Y_2  = 50

def generate_messy_data():
    data_1 = [(random.normalvariate(MESSY_MEAN_X_1, MESSY_STD_X_1),
               random.normalvariate(MESSY_MEAN_Y_1, MESSY_STD_Y_1)) for i in range(500)]
    data_2 = [(random.normalvariate(MESSY_MEAN_X_2, MESSY_STD_X_2),
               random.normalvariate(MESSY_MEAN_Y_2, MESSY_STD_Y_2)) for i in range(500)]

    return data_1, data_2, (data_1 + data_2)

#
# Script behavior
#
_, _, data = generate_messy_data()

for point in data:
    print str(point[0]) + "\t" + str(point[1])