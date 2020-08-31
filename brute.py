#!/usr/bin/env python3
import argparse
import zipfile

def getargs():
	parser = argparse.ArgumentParser()
	parser.add_argument("-f", "--file", dest="input_file", help="Name of the zip file to open", metavar="<filename>",required=True)
	parser.add_argument("-w", "--word-list", dest="word_list", help="Name of the word list to open", metavar="<filename>", required=True)
	parser.add_argument("-n","--number",dest="number",help="Define the ammount of numbers to add to the end of the password e.g. 9999", metavar="<integer>",default="0")
	return parser.parse_args()

def extract(zip_file,password):
	try:
		zip_file.extractall(pwd=bytes(password, encoding='utf-8'))
		return password
	except:
		return False

def cracker(zipFile_name,passwordFile_name):
	#Open Zip file using the name that was taken form the command line input
	zipFile = zipfile.ZipFile(zipFile_name)
	passwordFile = open(passwordFile_name)
	#Could load word file into array but that seems in-efficient
	for line in passwordFile.readlines():
		password = line.strip("\n")
		if extract(zipFile,password) != False:
			print("Password Found: ", password)
			exit()
	print("Password not found!")		

def cracker_with_numbers(zipFile_name,passwordFile_name,max_number):
	max_number = int(max_number)
	zipFile = zipfile.ZipFile(zipFile_name)
	passwordFile = open(passwordFile_name)
	for line in passwordFile.readlines():
		password = line.strip("\n")
		for i in range(0,max_number):
			new_password = password + str(i)
			if extract(zipFile,new_password) != False:
				print("Password Found: ", new_password)
				exit()
	print("Password not found!")

if __name__ == "__main__":
	arguments = getargs()
	if arguments.number != "0":
		print("-n added!")
		cracker_with_numbers(arguments.input_file,arguments.word_list, arguments.number)
	else:
		print("No additional options added!")
		cracker(arguments.input_file,arguments.word_list)