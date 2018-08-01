varA=input("Enter a stirng: ")
varB=input("Enter second string: ")
if isinstance(varA,str) or isinstance(varB,str):
	print("Strings involved")
elif varA>varB:
	print("bigger")
elif varA==varB:
	print("equal")
elif varA<varB:
	print("smaller")
