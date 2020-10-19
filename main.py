alphabet  [ chr(ord("a") + i) for i in range(26) ] # list of the alphabet (a-z)
reversed_alphabet = alphabet[::-1]
sorted_alphabet = alphabet.sort()
numbers_alphabet = [*(chr(ord("0") + i) for i in range(10)), *alphabet] # concatenate numbers and alphabets into 1 array (0-9,a-z)
