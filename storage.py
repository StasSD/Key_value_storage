import os
import tempfile
import json
import argparse
import sys

DEBUG = True


def load_data():

	storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')

	if (not os.path.exists(storage_path)):
		file = open(storage_path, "x")
		file.close()
		return dict() # returning empty dict

	else:
		with open(storage_path, "r") as storage:
		return data

def print_storage_file():
	storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')
	print(storage_path)


def key_check(key):
	if (arguments.key):
		return True
	else:
		return False

def value_check(value):
	if (arguments.value):
		return True
	else:
		return False

def print_list(list):
	for element in list:
		print(element, ' ')

def add_to_storage(data, key, value):

	if key in data:
		data[key].append(value) # appending value to existing list, otherwise creating new list at given key
		if DEBUG:
			print("Value ", value, "appended to list by key ", key)
	else:
		data[key] = list() # using list data structure to store multiple values at one key
		data[key].append(value)
		if DEBUG:
			print("New list created by key ", key, "added element with value: ", value)


	storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')

	with open(storage_path, "w") as debug_storage:
		json.dump(data, debug_storage)


def retrieve_from_storage(key):



	storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')
	if (not os.path.exists(storage_path)):
		print("")
		exit()

	with open(storage_path, "r") as debug_storage:
		data = json.load(debug_storage)

		if DEBUG:
			print("Extracted data: ", data)

		if key in data:

			#print("Obtained value: ")
			print_list(data[key])

		else:

			if DEBUG:
				print("No data corresponding to this key")
			print("") # empty string if no values were found by key




def get_arguments(data): # data is a dictionary which containes key-value information


	parser = argparse.ArgumentParser()
	parser.add_argument("--key")
	parser.add_argument("--value")
	args = parser.parse_args() #parsing arguments


	ARGS_CHK = False # flag for determining whether the input of arguments was correct

	if DEBUG:
		print("\n\n\n") # for easier log view

	if DEBUG:

		if (args.key and args.value):

			print("both key and val arguments passed")
			print("key argument:", args.key)
			print("value argument:", args.value, "\n\n\n")

		elif (args.key):

			print("only key argument passed")
			print("key argument:", args.key, "\n\n\n")

		elif (args.value):

			print("only value argument passed")
			print("value argument:", args.value, "\n\n\n")

		else:
			print("None of the arguments were passed", "\n\n\n")

	if (args.key and args.value):
		ARGS_CHK = True # input OK

		if DEBUG:
			print("key and value passed")
			print("key: ", args.key, "value: ", args.value, "\n\n\n")

		add_to_storage(data, args.key, args.value)

	elif (args.key and args.value == None):
		ARGS_CHK = True # input OK

		if DEBUG:
			print("key passed")
			print("key: ", args.key, "\n\n\n")

		retrieve_from_storage(args.key)

	elif (args.key == None and args.value):
		ARGS_CHK = False # input not OK

		print("Error: incorrect input.")
		print("Entering value without key is not allowed. Key option expected.", "\n\n\n")

	else:
		ARGS_CHK = False

		print("Error: incorrect input. Key option expected", "\n\n\n")

	if ARGS_CHK == False:
		print("Exit with error code 1", "\n\n\n")
		sys.exit(1)


def main(): #main function

	if DEBUG:
		print_storage_file()
	data = load_data() # load existing data from file
	get_arguments(data) # get arguments from input




main() #start of main function


