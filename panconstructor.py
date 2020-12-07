import hashlib 

print("Enter first 6 digits:")
first6 = input()
print("First 6 digits: " + first6)

print("Enter last 4 digits:")
last4 = input()
print("Last 4 digits: " + last4)

print("Enter half MD5 hash:")
half_hash = input()
print("Half of the MD5 hash: " + half_hash)

initialPAN = first6 + '000000' + last4
initialPAN = int(initialPAN)

for i in range(1000000): 
	hash_value_pan = hashlib.md5(str(initialPAN).encode()).hexdigest()
	half_hash_pan = hash_value_pan[0:len(hash_value_pan)//2]
	if half_hash_pan == half_hash:
		print("Constructed PAN: ")
		print(initialPAN)
	initialPAN += 10000
