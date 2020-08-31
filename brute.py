#!/usr/bin/env python3
import argparse
import zipfile

def getargs():
	parser = argparse.ArgumentParser()
	parser.add_argument("-f", "--file", dest="input_file", help="Name of the zip file to open", metavar="<filename>",required=True)
	parser.add_argument("-w", "--word-list", dest="word_list", help="Name of the word list to open", metavar="<filename>", required=True)
	return parser.parse_args()

def extract(zip_file,password):
	try:
		zip_file.extractall(pwd=bytes(password, encoding='utf-8'))
		return password
	except:
		return False

def cracker(zipFile_name,passwordFile):
	#Open Zip file using the name that was taken form the command line input
	zipFile = zipfile.ZipFile(zipFile_name)
	passwordFile = open(passwordFile)
	for line in passwordFile.readlines():
		password = line.strip("\n")
		if extract(zipFile,password) != False:
			print("Password Found:", password)
			exit(0)
	print("Password not found!")		

if __name__ == "__main__":
	arguments = getargs()
	cracker(arguments.input_file,arguments.word_list)