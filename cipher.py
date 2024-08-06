# add your code here

# given a word or a phrase, return an encrypted word or phrase with an alphabetical offset of 5. Ignore spaces and non-letter characters.

# Examples:
# abc -> efg
# xyz -> def
# aaa! -> eee!

# ask for a word or phrase to be encrypted
# for each character in the word,
	# if the character is not a letter
		# print the character
	# if the character is a letter
		# get the index of that character in the alphabet
		# example: a = 0
		# shift the index + 5
		# if the shifted index is < 26:
			# example shifted a = 5 -> e
			# print the shifted character 
		# else:
			# subtract or mod 26 from the shifted index

 # alpha  "abcdefghijklmnopqrstuvwxyz"
alpha = "abcdefghijklmnopqrstuvwxyz"
    
shift = input("abcdefghijklmnopqrstuvwxyz: ")
    
encrypted_shift = ""
    
for char in shift:
        if not char.isalpha():
            encrypted_shift += char
        else:
            index = alpha.index(char.lower())  # a = 0, b = 1, ...
            shifted_index = index + 5
            if shifted_index < 26:
                new_char = alpha[shifted_index]
            else:
                new_char = alpha[shifted_index % 26]

            if char.isupper():
                new_char = new_char.upper()
            
            encrypted_shift += new_char
    
print("Encrypted shift:", encrypted_shift)
