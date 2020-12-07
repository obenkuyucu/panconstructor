import hashlib 

def sum_digits(digit):
    if digit < 10:
        return digit
    else:
        sum = (digit % 10) + (digit // 10)
        return sum

def validate(cc_num):
    # reverse the credit card number
    cc_num = cc_num[::-1]
    # convert to integer list
    cc_num = [int(x) for x in cc_num]
    # double every second digit
    doubled_second_digit_list = list()
    digits = list(enumerate(cc_num, start=1))
    for index, digit in digits:
        if index % 2 == 0:
            doubled_second_digit_list.append(digit * 2)
        else:
            doubled_second_digit_list.append(digit)

    # add the digits if any number is more than 9
    doubled_second_digit_list = [sum_digits(x) for x in doubled_second_digit_list]
    # sum all digits
    sum_of_digits = sum(doubled_second_digit_list)
    # return True or False
    return sum_of_digits % 10 == 0

while True:
    try:
        first6 = int(input("Enter first 6 digits: "))
    except ValueError:
        print("Sorry, only integers")
        continue
    else:
        break
first6 = str(first6)
print("First 6 digits: " + first6)

while True:
    try:
        last4 = int(input("Enter last 4 digits: "))
    except ValueError:
        print("Sorry, only integers")
        continue
    else:
        break
last4 = str(last4)
print("Last 4 digits: " + last4)

hash_str = input("Enter any string of MD5 hash: ")
print("Provided MD5 hash strings: " + hash_str)

initialPAN = first6 + '000000' + last4
initialPAN = int(initialPAN)
tot_pan = 0
print("Constructed PAN(s): ")
for i in range(1000000): 
	hash_value_pan = hashlib.md5(str(initialPAN).encode()).hexdigest()
	split_hash_pan = hash_value_pan[0:len(hash_str)]
	if split_hash_pan == hash_str:
		if validate(str(initialPAN)):
			print(initialPAN)
			tot_pan = tot_pan + 1
	initialPAN += 10000
print("Total constructed PAN(s): " + format(tot_pan))
