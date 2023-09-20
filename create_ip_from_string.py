"""
You're given a string of length 12 or smaller,containing only digits.Write a function that returns all the possible IP addresses that can be created by inserting .s in the string.
An IP address is a sequence of four positive integers that are seperated by .s,where each individual integer is within the range 0-255,inclusive
An IP address isnt valid if any of the individual integers conatining leading 0s.For example "192.168.1.1" , "192.168.1.0","192.168.0.1" are valid IP addresses but "192.168.01.1", "192.168.1.00","192.168.00.1"  are invalid Ip addresses because they contain "00" and "01" respectively.Another example of valid IP address is "99.1.1.10" but "991:1.1.0" isnt valid because "991" is greater than 255.
Your function should return the IP address in string format and in no particular order .If no valid IP address can be created from the string your function should return an empty list.
Sample Input
string ="1921680"
Sample output
[
"1.9.216.80",
"1.92.16.80",
"1.92.168.0",
"19.2.16.80",
"19.2.168.0",
"19.21.6.80",
"19.21.68.0",
"19.216.8.0",
"192.1.6.80",
"192.1.68.0",
"192.16.8.0"
]
"""


#each individual integer is within the range 0-255
def valid_octat(num):
	if len(num) > 1 and int(num[:1])==0:
		return False
	if int(num) >= 0 and int(num) <=255:
		return True
	return False

#Example - 1921680
#Further optimize by adding the validity check at each octat level.

def create_ip(input_str):
	ip_address_list = [] 
	for i in range (1,4): # i=j=k=1 ->> first_octat=1, second_octat=9, third_octat=2, fourth_octat=1680
		first_octat = input_str[0:i]
		for j in range(1,4):
			second_octat = input_str[i:i+j]
			for k in range(1,4):
				third_octat = input_str[i+j:i+j+k]
				fourth_octat = input_str[i+j+k:]
				if valid_octat(first_octat) and valid_octat(second_octat) and valid_octat(third_octat) and valid_octat(fourth_octat):
					ip_address_list.append(first_octat+'.'+second_octat+'.'+third_octat+'.'+fourth_octat)
	return ip_address_list
