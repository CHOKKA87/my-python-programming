n=int(input("enter  a number"))
while n>0:
	rem=n%10
	rev=rem*10
	n=n//10
print(rev)
