
def NRICinput():
	NRIC=input("Please key in Valid NRIC ID to verify:\n")
	str(NRIC)
	return NRIC.upper()

def NRICcheck(NRIC):
	i=1
	Begin=["S","T","F","G"]
	if NRIC[0] in Begin:
		Bflag=1
	else:
		Bflag=0

	if NRIC[0].isalpha()!=1 or NRIC[8].isalpha()!=1 or Bflag!= 1:
		NRIC=NRICinput()
	
	for i in range(len(NRIC)-2):
		if NRIC[i].isnumeric()!=1:
			NRIC=NRICinput()
	return NRIC
		
def NRIClencheck(NRIC):
	if len(NRIC)!=9:
		NRIC=NRICinput()
	return NRIC.upper()

def STchecksum(Ssum,last):
	alphalist=["J","Z","I","H","G","F","E","D","C","B","A"]
	if last==alphalist[Ssum]:
		print('valid\n')
		flag=0
	else:
		print('Wrong ID or Fake!\n')
		#input()
		flag=1
	return flag

def FGchecksum(Ssum,last):
	alphalist=["X","W","U","T","R","Q","P","N","M","L","K"]
	if last==alphalist[Ssum]:
		print('valid\n')
		flag=0
	else:
		print('Wrong ID or Fake!\n')
		#input()
		flag=1
	return flag

def main():
	flag=0
	try:
		NRIC=NRICinput()
	except:
		NRIC=NRICinput()
		
	while len(NRIC)!=9:
		NRIC=NRIClencheck(NRIC)
		NRIC=NRICcheck(NRIC)
	
	#Ssum=(int(NRIC[1])*2+int(NRIC[2])*7+int(NRIC[3])*6+int(NRIC[4])*5+int(NRIC[5])*4+int(NRIC[6])*3+int(NRIC[7])*2)%11
	last=NRIC[8]
	
	if NRIC[0]=="S":
		Ssum=(int(NRIC[1])*2+int(NRIC[2])*7+int(NRIC[3])*6+int(NRIC[4])*5+int(NRIC[5])*4+int(NRIC[6])*3+int(NRIC[7])*2)%11
		flag=STchecksum(Ssum,last)
		
	if NRIC[0]=="T":
		Ssum=(int(NRIC[1])*2+int(NRIC[2])*7+int(NRIC[3])*6+int(NRIC[4])*5+int(NRIC[5])*4+int(NRIC[6])*3+int(NRIC[7])*2+4)%11
		flag=STchecksum(Ssum,last)

	if NRIC[0]=="G":
		Ssum=(int(NRIC[1])*2+int(NRIC[2])*7+int(NRIC[3])*6+int(NRIC[4])*5+int(NRIC[5])*4+int(NRIC[6])*3+int(NRIC[7])*2+4)%11
		flag=FGchecksum(Ssum,last)
	if NRIC[0]=="F":
		Ssum=(int(NRIC[1])*2+int(NRIC[2])*7+int(NRIC[3])*6+int(NRIC[4])*5+int(NRIC[5])*4+int(NRIC[6])*3+int(NRIC[7])*2)%11
		flag=FGchecksum(Ssum,last)
	
	if NRIC[0]=="T":
		YOB="20"+NRIC[1]+NRIC[2]
	else:
		if NRIC[0]=="S" and int(NRIC[1])<2:
			YOB="Prior to 1968"
		else:
			if NRIC[0]=="S":
				YOB="19"+NRIC[1]+NRIC[2]
			else:
				if NRIC[0]=="G":
					YOB="ID issued in 20"+NRIC[1]+NRIC[2]
				else:
					if NRIC[0]=="F":
						YOB="ID issued before 2000 and born on 19"+NRIC[1]+NRIC[2]
					else:
						flag=1
						print("Wrong ID! Not Valid")
	if flag==0:
		print('YOB: '+YOB+'\n'+'Your ID seems valid...\n')
try:	
	main()
except:
	main()	
input()