# list of the alphabet (a-z)
alphabet = [ chr(ord("a") + i) for i in range(26) ]
reversed_alphabet = alphabet[::-1]
sorted_alphabet = alphabet.sort()
#concatenate numbers and alphabets into 1 array (0-9,a-z)
numbers_alphabet = [*(chr(ord("0") + i) for i in range(10)), *alphabet]
