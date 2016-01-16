#Matthia Cognitive Model Python Version	1.0

#The idea is that when your time estimation (that is given by the DM + blending)
#is lower then the time stimuli presented by the experiment I perform better because I'm already
#ready, on the other side if it's higher I "get surprised" and perform worst, add a penality
#to the computational model....I perform worst since I need to recap and press the button when I thought I wasn't
#going to...

#The general idea behind the model is to test if previous trials have an influence on the performances during 
#the next trials.


import numpy as np
import random
import math
import csv

actr_a = 1.1
actr_b = 0.015
actr_t0 = 11
actr_decay_rate = 0.5

num_subjects = 18 #According to the .csv file
num_sessions = 5
num_trials = 120


def plot_existing_data():
	
	with open ('#name.csv', 'rb') as csvfile:
		data = csv.reader(csvfile, delimiter=' ', quotechar='|') #FIXME when you have the data
		for row in in data:
			print(', '.join(row))


def create_declarative_memory(chunks):

	Declarative_Memory = [[] for i in range(1,chunks+1)]	#list of empty lists according to the number of chunks

	return Declarative_Memory


def update_declarative_memory(dm, pulse,time):

	dm[pulse].append(time)


def get_encounters(dm, pulse):

	return dm[pulse]


def actr_b(encounters, current_time):
	
	assert(current_time >= max(encounters), "ERROR!")	#assert function skips if the code is correctly otherwise error message

	delta_times = [current_time - i for i in encounters]
	powered_times = [i**-actr_decay_rate for i in delta_times]

	return math.log(sum(powered_times))


def blending(dm,current_time):

	activations = []
	tot = 0

	for p in range(1,len(dm)):
		enc = get_encounters(dm, p)
		activations.append(actr_b(enc,current_time))

	for i in range(1,len(activations)):
		tot += i*activations[i-1]

	blended_value = tot/sum(activations)
	
	return blended_value


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

	return uni_vec



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

	return expo_vec


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

	return anti_expo_vec

	

def actr_noise(s):	#noise function that produces some randomness while running the experiment

	n_random = random.uniform(0.0001, 0.9999)
	s*math.log((1-n_random)/n_random)

	return s

def pulse_into_time(num_pulses): #converts number of pulses into time

	interval_estimation = actr_t0
	global_time = actr_t0

	for i in range (1,num_pulses):
		interval_estimation = interval_estimation * actr_a + actr_noise(actr_a * actr_b * interval_estimation)
		global_time = global_time + interval_estimation

	return global_time


def time_into_pulse(time):	#converts time intervals into pulses

	interval_estimation = actr_t0
	num_pulses = 0
	time_tracker = actr_t0

	while time_tracker < time:
		interval_estimation = interval_estimation * actr_a + actr_noise(actr_a * actr_b * interval_estimation)
		time_tracker = time_tracker + interval_estimation
		num_pulses = num_pulses + 1

	return num_pulses


def run_model(num_subjects, num_sessions):

	for i in range(1,num_subjects):

		subject_clock = 0
		subject_DM = create_declarative_memory(120,120) #number of chunks and encounters, 120 because
														#of the 4 different foreperiods and relative estimations 
		for j in range(1, num_sessions):

			if(j=1 or j=3 or j=5):

				uniform_foreperiod = uniform_condition(30)

				for time in uniform_foreperiod:
					subject_clock = subject_clock + time 
					pulse_estimation = time_into_pulse(subject_clock)
					blended_value = blending(subject_DM, subject_clock) #check what the function gets as input
					blended_value_converted = pulse_into_time(blended_value_converted)

					if blended_value_converted > pulse_estimation:
						subject_clock = subject_clock + 50 #penality of 5000 ms added 
						update_declarative_memory(subject_DM, pulse_estimation, subject_clock)
					else:
						update_declarative_memory(subject_DM, pulse_estimation, subject_clock)
					#run the uniform condition
			
			elif(j=2):

				exponential_foreperiod = exponential_condition(64,32,16,8)
				
				for time in exponential_foreperiod:
					subject_clock = subject_clock + random.uniform(250,850) + time
					pulse_estimation = time_into_pulse(subject_clock)
					blended_value = blending(subject_DM, subject_clock) 
					blended_value_converted = pulse_into_time(blended_value)

					if blended_value_converted > time :
						subject_clock = subject_clock + 50 #penality of 5000 ms added 
						update_declarative_memory(subject_DM, pulse_estimation, subject_clock)
					else:
						update_declarative_memory(subject_DM, pulse_estimation, subject_clock)
					#run the exponential condition
			
			elif(j=4):
				
				antiexponential_foreperiod = anti_exponential_condition(8,16,32,64)
				
				for time in antiexponential_foreperiod:
					subject_clock = subject_clock + random.uniform(250,850) + time
					pulse_estimation = time_into_pulse(subject_clock)					
					blended_value = blending(subject_DM, subject_clock) 
					blended_value_converted = pulse_into_time(blended_value)

					if blended_value_converted > pulse_estimation:
						subject_clock = subject_clock + 50 #penality of 5000 ms added 
						update_declarative_memory(subject_DM, pulse_estimation, subject_clock)
					else:
						update_declarative_memory(subject_DM, pulse_estimation, subject_clock)
					
				#run the antiexponential condition 


if __name__ == "__main__":





"""FIXME the results aren't perfectly matching with the R function
But the code still seems correct, check the 2 functions separetly once the model is working
"""