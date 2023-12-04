# Write a Python program to test whether a passed letter is a vowel or not.
letter  = input("Input a Letter of The Alphabet : ")

if letter  in ('a', 'e', 'i', 'o', 'u','A', 'E', 'I', 'O', 'U'):
	print(letter ,"is a vowel.")
else:
	print(letter ,"is a consonant.")
