import numpy as np
import math
from numpy import *


# define constants used like flags
NUMBER_OF_INSTANCES = 100000

USING_FIRST_DRAGON = 1
USING_FIRST_INHIBITOR = 1
USING_FIRST_RIFT_HERALD = 1
USING_FIRST_BARON = 1
USING_BARON_KILLS = 1
USING_RIFT_HERALD_KILLS = 1
USING_FIRST_BLOOD = 1
USING_FIRST_TOWER = 1
USING_INHIBITOR_KILLS = 1
USING_TOWER_KILLS = 1
USING_DRAGON_KILLS = 1

RIDGE_REGRESSION_INSTEAD_OF_LINEAR_REGRESSION = 0
GRADIENT_DESCENT_INSTEAD_OF_CLOSED_FORM_SOLUTION = 0

PERCENT_TRAIN = 0.8
NUMBER_OF_TRAINING_INSTANCES = int(NUMBER_OF_INSTANCES*0.8)
NUMBER_OF_TEST_INSTANCES = NUMBER_OF_INSTANCES - NUMBER_OF_TRAINING_INSTANCES


NUMBER_OF_FEATURES = USING_FIRST_DRAGON + USING_FIRST_INHIBITOR + USING_FIRST_RIFT_HERALD + USING_FIRST_BARON + USING_BARON_KILLS + USING_RIFT_HERALD_KILLS + USING_FIRST_BLOOD + USING_FIRST_TOWER + USING_INHIBITOR_KILLS + USING_TOWER_KILLS + USING_DRAGON_KILLS

#
# ACCESSING DATA
#

# open input file and output file
data = open('matchHistory.txt','r')
results = open('results.txt','w+')

# initialize matrices
x_train = np.zeros((NUMBER_OF_TRAINING_INSTANCES, NUMBER_OF_FEATURES+1))
w = np.zeros(( (NUMBER_OF_FEATURES+1) ,1))
y_train = np.zeros((NUMBER_OF_TRAINING_INSTANCES,1))

x_test = np.zeros((NUMBER_OF_TEST_INSTANCES, NUMBER_OF_FEATURES+1))
y_test = np.zeros((NUMBER_OF_TEST_INSTANCES,1))

# format training data
feature_string = ''
for i in range(NUMBER_OF_TRAINING_INSTANCES):
	line = data.readline()
	split_line = line.split(',')
	if split_line[0]!= '':
		win 				= int(split_line[0])
	else:
		win = 0
	if split_line[1]!= '':
		first_dragon 		= int(split_line[1])
	else:
		first_dragon = 0
	if split_line[2]!= '':
		first_inhibitor 	= int(split_line[2])
	else:
		first_inhibitor = 0
	if split_line[3]!= '':
		first_rift_herald 	= int(split_line[3])
	else:
		first_rift_herald = 0
	if split_line[4]!= '':
		first_baron 		= int(split_line[4])
	else:
		first_baron = 0
	if split_line[5]!= '':
		baron_kills 		= int(split_line[5])
	else:
		baron_kills = 0
	if split_line[6]!= '':
		rift_herald_kills 	= int(split_line[6])
	else:
		rift_herald_kills
	if split_line[7]!= '':
		first_blood 		= int(split_line[7])
	else:
		first_blood = 0
	if split_line[8]!= '':
		first_tower 		= int(split_line[8])
	else:
		first_tower = 0
	if split_line[9]!= '':
		inhibitor_kills		= int(split_line[9])
	else:
		inhibitor_kills = 0
	if split_line[10]!= '':
		tower_kills 		= int(split_line[10])
	else:
		tower_kills = 0
	if split_line[11]!= '':
		dragon_kills 		= int(split_line[11])
	else:
		dragon_kills = 0
	
	y_train[i] = win*100

	j = 0
	feature_string = ''
	if USING_FIRST_DRAGON == 1:
		feature_string += '1st_drag\t'
		x_train[i][j] = first_dragon
		j += 1
	if USING_FIRST_INHIBITOR == 1:
		feature_string += '1st_inhb\t'
		x_train[i][j] = first_inhibitor
		j += 1
	if USING_FIRST_RIFT_HERALD == 1:
		feature_string += '1st_rher\t'
		x_train[i][j] = first_rift_herald
		j += 1
	if USING_FIRST_BARON == 1:
		feature_string += '1st_bar\t\t'
		x_train[i][j] = first_baron
		j += 1
	if USING_BARON_KILLS == 1:
		feature_string += 'bar_kills\t'
		x_train[i][j] = baron_kills 
		j += 1
	if USING_RIFT_HERALD_KILLS == 1:
		feature_string += 'rher_kills\t'
		x_train[i][j] = rift_herald_kills
		j += 1
	if USING_FIRST_BLOOD == 1:
		feature_string += '1st_bld\t\t'
		x_train[i][j] = first_blood
		j += 1
	if USING_FIRST_TOWER == 1:
		feature_string += '1st_twr\t\t'
		x_train[i][j] = first_tower
		j += 1
	if USING_INHIBITOR_KILLS == 1:
		feature_string += 'inh_kills\t'
		x_train[i][j] = inhibitor_kills
		j += 1
	if USING_TOWER_KILLS == 1:
		feature_string += 'twr_kills\t'
		x_train[i][j] = tower_kills
		j += 1
	if USING_DRAGON_KILLS == 1:
		feature_string += 'drag_kills\t'
		x_train[i][j] = dragon_kills
		j += 1
	x_train[i][j] = 1

# test print training data
print "num\t\ty_train\t\t",feature_string
for i in range(NUMBER_OF_TRAINING_INSTANCES):
	print i,"\t\t",y_train[i][0],"\t\t",
	for j in range(NUMBER_OF_FEATURES+1):
		print x_train[i][j],"\t\t",
	print "\n",

# format test data
for i in range(NUMBER_OF_TEST_INSTANCES):

	line = data.readline()
	split_line = line.split(',')

	if split_line[0]!= '':
		win 				= int(split_line[0])
	else:
		win = 0
	if split_line[1]!= '':
		first_dragon 		= int(split_line[1])
	else:
		first_dragon =0
	if split_line[2]!= '':
		first_inhibitor 	= int(split_line[2])
	else:
		first_inhibitor = 0
	if split_line[3]!= '':
		first_rift_herald 	= int(split_line[3])
	else:
		first_rift_herald = 0
	if split_line[4]!= '':
		first_baron 		= int(split_line[4])
	else:
		first_baron = 0
	if split_line[5]!= '':
		baron_kills 		= int(split_line[5])
	else:
		baron_kills = 0
	if split_line[6]!= '':
		rift_herald_kills 	= int(split_line[6])
	else:
		rift_herald_kills = 0
	if split_line[7]!= '':
		first_blood 		= int(split_line[7])
	else:
		first_blood = 0
	if split_line[8]!= '':
		first_tower 		= int(split_line[8])
	else:
		first_tower = 0
	if split_line[9]!= '':
		inhibitor_kills		= int(split_line[9])
	else:
		inhibitor_kills = 0
	if split_line[10]!= '':
		tower_kills 		= int(split_line[10])
	else:
		tower_kills = 0
	if split_line[11]!= '':
		dragon_kills 		= int(split_line[11])
	else:
		dragon_kills = 0
	
	y_test[i] = win*100

	j = 0
	feature_string = ''
	if USING_FIRST_DRAGON == 1:
		feature_string += '1st_drag\t'
		x_test[i][j] = first_dragon
		j += 1
	if USING_FIRST_INHIBITOR == 1:
		feature_string += '1st_inhb\t'
		x_test[i][j] = first_inhibitor
		j += 1
	if USING_FIRST_RIFT_HERALD == 1:
		feature_string += '1st_rher\t'
		x_test[i][j] = first_rift_herald
		j += 1
	if USING_FIRST_BARON == 1:
		feature_string += '1st_bar\t\t'
		x_test[i][j] = first_baron
		j += 1
	if USING_BARON_KILLS == 1:
		feature_string += 'bar_kills\t'
		x_test[i][j] = baron_kills 
		j += 1
	if USING_RIFT_HERALD_KILLS == 1:
		feature_string += 'rher_kills\t'
		x_test[i][j] = rift_herald_kills
		j += 1
	if USING_FIRST_BLOOD == 1:
		feature_string += '1st_bld\t\t'
		x_test[i][j] = first_blood
		j += 1
	if USING_FIRST_TOWER == 1:
		feature_string += '1st_twr\t\t'
		x_test[i][j] = first_tower
		j += 1
	if USING_INHIBITOR_KILLS == 1:
		feature_string += 'inh_kills\t'
		x_test[i][j] = inhibitor_kills
		j += 1
	if USING_TOWER_KILLS == 1:
		feature_string += 'twr_kills\t'
		x_test[i][j] = tower_kills
		j += 1
	if USING_DRAGON_KILLS == 1:
		feature_string += 'drag_kills\t'
		x_test[i][j] = dragon_kills
		j += 1
	x_test[i][j] = 1




#
# TRAINING
#

x_train = np.matrix(x_train)
y_train = np.matrix(y_train)
w = np.matrix(w)

# find lambda in case of ridge regression
if RIDGE_REGRESSION_INSTEAD_OF_LINEAR_REGRESSION:
	# TODO: Find lambda
	training_lambda = 0

# set lambda in case of linear regression
# using lambda != 0, but very small to guarantee invertible matrix to calculate w
else:
	training_lambda = 1e-14

# test print lambda
print "lambda used: ",training_lambda

# calculate w in case of gradient descent
if GRADIENT_DESCENT_INSTEAD_OF_CLOSED_FORM_SOLUTION:
	# TODO: Find w
	w = np.zeros(( (NUMBER_OF_FEATURES+1) ,1))

# calculate w in case of closed form solution
else:
	w = np.linalg.inv(x_train.T * x_train + training_lambda*np.eye(NUMBER_OF_FEATURES+1)) * x_train.T * y_train
	



#
# TESTING
#

x_test = np.matrix(x_test)
y_test = np.matrix(y_test)

# test data RMSE
y_test_new = x_test * w
y_difference = y_test_new - y_test
y_diff_squared = y_difference.T * y_difference
RMSE_test = sqrt(y_diff_squared/NUMBER_OF_TEST_INSTANCES)

print "test RMSE: ", RMSE_test

# training data RMSE
y_train_new = x_train * w
y_difference = y_train_new - y_train
y_diff_squared = y_difference.T * y_difference
RMSE_train = sqrt(y_diff_squared/NUMBER_OF_TRAINING_INSTANCES)

print "training RMSE: ", RMSE_train

# print w
w = np.array(w)
print feature_string
print "w: "
for i in range(NUMBER_OF_FEATURES):
	print w[i][0],"\t",

print "\n",




































































































