import random 
import array 

# maximum length of password needed 
MAX_LEN = 12

DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] 
LOCASE_CHARACTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 
					'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q', 
					'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 
					'z'] 

UPCASE_CHARACTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 
					'I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q', 
					'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 
					'Z'] 

SYMBOLS = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>', 
		'*', '(', ')', '<'] 

# combines all the character arrays above to form one array 
COMBINED_LIST = DIGITS + UPCASE_CHARACTERS + LOCASE_CHARACTERS + SYMBOLS 

# randomly select at least one character from each character set above 
rand_digit = random.choice(DIGITS) 
rand_upper = random.choice(UPCASE_CHARACTERS) 
rand_lower = random.choice(LOCASE_CHARACTERS) 
rand_symbol = random.choice(SYMBOLS) 

temp_pass = rand_digit + rand_upper + rand_lower + rand_symbol 

for x in range(MAX_LEN - 4): 
	temp_pass = temp_pass + random.choice(COMBINED_LIST) 

	temp_pass_list = array.array('u', temp_pass) 
	random.shuffle(temp_pass_list) 

# the lines of code below is to store the each character of temp_pass_list in the password variable where there might 
# be existing password

password = "Himal" #This code might be vary depending upon the users
for x in temp_pass_list: 
		password = password + x 
		
# print out password
print("Your generated password is:", password) 
