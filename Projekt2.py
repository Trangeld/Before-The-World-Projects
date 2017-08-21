Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:14:34) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import sys
>>> def add ():
	i=0
	j=True
	x=0
	y=0
	z=False
	w='-'
	print ("Please put in a number then press Enter then Ctrl-D: ")
	num=str(sys.stdin.readlines())
	if len(num)==0:
		print("0")
	if len(num)<3:
		try:
			x=int(num)
			if x<0:
				raise ValueError("negatives not allowed")
			print(x)
		except:
        		print("The sum of the numbers inserted is "+str(x))
	if len(num)>2:
		while i<len(num):
			try:
				if j==True:
					x*=10
				x+=int(num[i])
				if y<0:
					y*=10
					y-=x
					x=0
				try:
					if z==True:
						z=False
						raise ValueError("negatives not allowed")
				except:
					print("You have entered a negative number: ")
					y=-x
					x=0
				i+=1
				j=True
			except:
				if j==True:
					x/=10
				if y<0:
					print(y)
					y=0
				j=False
				z=False
				if z==False:
					if num[i]=='-':
						z=True
				if x>1000:
					x=0
				i+=1
				y+=x
				x=0
				continue
		y+=x
		y=int(y)
		x=y
		print("The sum of the numbers inserted is "+str(x))

		
>>> add()
Please put in a number then press Enter then Ctrl-D: 
The sum of the numbers inserted is 0
>>> add()
Please put in a number then press Enter then Ctrl-D: 
1
The sum of the numbers inserted is 1
>>> add()
Please put in a number then press Enter then Ctrl-D: 
1,2
The sum of the numbers inserted is 3
>>> add()
Please put in a number then press Enter then Ctrl-D: 
1,2,3,4,5
The sum of the numbers inserted is 15
>>> add()
Please put in a number then press Enter then Ctrl-D: 
1
2
3
4
The sum of the numbers inserted is 10
>>> add()
Please put in a number then press Enter then Ctrl-D: 
-1
You have entered a negative number: 
-1
The sum of the numbers inserted is 0
>>> add()
Please put in a number then press Enter then Ctrl-D: 
-1-2,-8
You have entered a negative number: 
-1
You have entered a negative number: 
-2
You have entered a negative number: 
-8
The sum of the numbers inserted is 0
>>> add()
Please put in a number then press Enter then Ctrl-D: 
500001
The sum of the numbers inserted is 0
>>> add()
Please put in a number then press Enter then Ctrl-D: 
//[***]\n1***2***3
The sum of the numbers inserted is 6
>>> add()
Please put in a number then press Enter then Ctrl-D: 
//[*][%]\n1*2%3
The sum of the numbers inserted is 6
>>> add()
Please put in a number then press Enter then Ctrl-D: 
//[***/][%%%+§]\n1***/2%%%+§3
The sum of the numbers inserted is 6
