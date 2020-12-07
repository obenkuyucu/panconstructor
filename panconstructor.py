import hashlib 
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
		print(initialPAN)
		tot_pan = tot_pan + 1
	initialPAN += 10000
print("Total constructed PAN(s): " + format(tot_pan))
