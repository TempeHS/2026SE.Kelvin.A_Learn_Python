def convert(time):
	hrs = float(time.split(":")[0])
	min = float(time.split(":")[1]) / 60
	return hrs + min

def main():
	timein = input("What Time: ")
	if convert(timein) <= 8 and convert(timein) >= 7:
		print("breakfast time")
	elif convert(timein) <= 13 and convert(timein) >= 12:
		print("lunch time")
	elif convert(timein) <= 19 and convert(timein) >= 18:
		print("dinner time")
	else:
		print("nothing")



if __name__ == "__main__":	    
    main()	