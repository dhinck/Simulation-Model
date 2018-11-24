# Darcy Hinck

import random as rnd


def TravelTime():
	return rnd.gauss(30, 5)

def TrafficTravel():
	return rnd.gauss(35, 10)

def ClassStart():
	return rnd.uniform(0, 5)
						   

NSIM = 10000

#BSIM1 = 3333
#BSIM2 = 6667

def HowEarlyToLeave():
	instances_of_arrival = []
	for i in range(NSIM):
		travel_time = TravelTime()
		class_start = ClassStart()

		instances_of_arrival.append(travel_time - class_start)

	instances_of_arrival.sort()

	number_of_minutes = instances_of_arrival[9500]

	return number_of_minutes


#print(HowEarlyToLeave())


def HowEarlyToLeaveBonus():

	instances_of_arrival = []

	for i in range(NSIM):
		class_start = ClassStart()

		number = rnd.randint(1, 3)
		if number == 1 :
			traffic_time = TrafficTravel()
			instances_of_arrival.append(traffic_time - class_start)

		else:
			travel_time = TravelTime()
			instances_of_arrival.append(travel_time - class_start)

	instances_of_arrival.sort()
	number_of_minutes = instances_of_arrival[9500]

	return number_of_minutes

#print(HowEarlyToLeaveBonus())


#	This is another solution to the bonus, but it relies on an exact number 
#	of traffic instances and an exact number of regular instances

#	instances_of_arrival = []
#	for i in range(BSIM1):
#		class_start = ClassStart()
#		traffic_time = TrafficTravel()
#
#		instances_of_arrival.append(traffic_time - class_start)
#
#	for i in range(BSIM2):
#		travel_time = TravelTime()
#		class_start = ClassStart()
#
#		instances_of_arrival.append(travel_time - class_start)
#
#	instances_of_arrival.sort()
#
#	number_of_minutes = instances_of_arrival[9500]
#
#	return number_of_minutes




