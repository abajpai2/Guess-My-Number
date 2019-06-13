low=0
high=101
ans=(low+high)/2.0
userinput= ''

while userinput!= 'c':
	print("Is your secret number" +' '+ str(round(ans))+ "?")	
	userinput = input("Entraaar 'h','l' or 'c' madarchod : ")
	
	if userinput == 'l':
		low = ans
	
	if userinput == 'h':
		high = ans
	
	ans=round((low+high)/2.0)
	
print("Good job butthole, your secret number is" + str(ans))


