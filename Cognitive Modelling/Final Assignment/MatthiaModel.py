#Matthia Cognitive Model Python Version


import numpy as np
import random
import math

actr_a = 1.1
actr_b = 0.015
actr_t0 = 11

num_subjects = 18 #According to the .csv file
num_sessions = 5
num_trials = 120


def plot_existing_data():




def declarative_memory():



def uniform_condition(a):

	conc_vector = []

	vec_a = []
	vec_b = []
	vec_c = []
	vec_d = []

	for i in range(a):
		vec_a.append(400)
		vec_b.append(800)
		vec_c.append(1200)
		vec_d.append(1600)

	conc_vector = np.concatenate(vec_a,vec_b,vec_c,vec_d)
	uniform_vector = np.random.shuffle(conc_vector)



def exponential_condition(a,b,c,d):

	conc_vector = []

	vec_a = []
	vec_b = []
	vec_c = []
	vec_d = []

	for i in range(a):
		vec_a.append(400)

	for j in range(b):
		vec_b.append(800)

	for k in range(c):
		vec_c.append(1200)

	for m in range(d):
		vec_d.append(1600)

	conc_vector = np.concatenate(vec_a,vec_b,vec_c,vec_d)
	expo_vector = np.random.shuffle(conc_vector)

	


def anti_exponential_condition(a,b,c,d):

	conc_vector = []

	vec_a = []
	vec_b = []
	vec_c = []
	vec_d = []

	for i in range(a):
		vec_a.append(400)

	for j in range(b):
		vec_b.append(800)

	for k in range(c):
		vec_c.append(1200)

	for m in range(d):
		vec_d.append(1600)

	conc_vector = np.concatenate(vec_a,vec_b,vec_c,vec_d)
	anti_expo_vector = np.random.shuffle(conc_vector)

	

def actr_noise(s):

	n_random = random.uniform(0.0001, 0.9999)
	s*math.log((1-n_random)/n_random)

	return s

def pulse_into_time(num_pulses):

	interval_estimation = actr_t0
	global_time = actr_t0

	for i in range (1,num_pulses):
		interval_estimation = interval_estimation * actr_a + actr_noise(actr_a * actr_b * interval_estimation)
		global_time = global_time + interval_estimation

	return global_time


def time_into_pulse(time):

	interval_estimation = actr_t0
	num_pulses = 0
	time_tracker = actr_t0

	while time_tracker < time:
		interval_estimation = interval_estimation * actr_a + actr_noise(actr_a * actr_b * interval_estimation)
		time_tracker = time_tracker + interval_estimation
		num_pulses = num_pulses + 1

	return num_pulses


def run_model():

	for i in range(1,num_subjects):

		for j in range(1, num_sessions):

			if(j=1 or j=3 or j=5):
				#run the uniform condition
			elif(j=2):
				#run the exponential condition
			elif(j=4):
				#run the antiexponential condition 


if __name__ == "__main__":

	for i in range(1,10):
		global_time = pulse_into_time(i)
		num_pulses = time_into_pulse(global_time)

		print(i, global_time, num_pulses)

"""FIXME the results aren't perfectly matching with the R function
But the code still seems correct
"""