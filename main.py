# list of the alphabet (a-z)
alphabets = [ chr(ord("a") + i) for i in range(26) ]

# list of the alphabet in reverse
reversed_alphabets = alphabets[::-1]

# list of numbers (1-100)
numbers = list(range(101))

# swap 2 variables
alphabets, numbers = numbers, alphabets
