stop = 0
passengers = 0

while passengers < 165:
	stop += 1
	if stop % 2 != 0:
		passengers += 11
	elif stop % 2 == 0:
	    passengers -= 5
print(stop)