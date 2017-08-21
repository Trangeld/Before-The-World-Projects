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
				print("You have entered a negative number " + x)
				raise ValueError("negatives not allowed")
		except:
        		print("Character that you have inserted is not a number")
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
		x=int(y)
		if y==0:
			print("Characters that you have inserted are not poitive numbers")
		else: print(x)
