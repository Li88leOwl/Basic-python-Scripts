# re for regular expressions 
#syntax 
# . any character except a newline 
# * 0 or more repetitions 
# + 1 or more repetitíons 
# ? 0 or 1 repetitions 
# {m} m repetitions 
# {m,n} m-n repetitions
#re.search(pattern, string , flags=0(re.IGNORECASE, re.MULTILINE, re.DOTALL))
# ^ matches the start of the string 
# $ matches the end of the string or just before the new line at the end of the string 
# [] allows you to type in a set of characters 
# [^] complementing set of characters you specifically exclude 
import re 
email = input("What's your student email address? ").strip()
if re.search(r'^[^@]+@[^@]+\.(com|edu|net|org|ke)$', email):
    print("Valid")
else:
    print("Invalid")
    
