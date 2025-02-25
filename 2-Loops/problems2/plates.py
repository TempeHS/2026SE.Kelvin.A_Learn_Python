def main():
	plate = input("Plate: ")
	if is_valid(plate):
		print("Valid")
	else:
		print("Invalid")


def is_valid(s): 
    return all([
    two_letters(s),	
	min_max_char(s),
	number_check(s),
    special_char(s),
	alpha_after_digits(s)
])

# checks if the first two characters are letters
def two_letters(s):
	if s[:2].isalpha():
		return True
	else:
		return False

# checks if the plate has 6 characters or less than 2 characters
def min_max_char(s):
	if len(s) >= 2 and len(s) <= 6:
		return True
	else:
		return False	

# checks if digits are after the first two letters and doesnt start with 0
def number_check(s):
	if s[4:].isdigit():
		return True
	else:
		return False	

# checks if there are any special characters
def special_char(s):
	if s[:6].isalnum():
		return False
	else:
		return True


# checks if any alphabets after the digits
def alpha_after_digits(s):
	for i in range(len(s)):
		if s[i].isdigit():
			for j in range(i + 1 , len(s)):
				if s[j].isalpha():
					return False
		return True




main()
