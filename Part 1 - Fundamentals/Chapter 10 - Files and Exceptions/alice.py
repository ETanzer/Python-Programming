def count_words(filename):

	try:
		with open(filename, encoding='utf-8') as f_obj:
			contents = f_obj.read()

	except FileNotFoundError:
		msg = "Sorry, the file " + filename + " does not exist or could not be found."
		print(msg)

	else:
		# Count the approximate number of words in a text file.
		words = contents.split()
		num_words = len(words)
		print("The file " + filename + " has about " + str(num_words) + " words.")
	
filename = 'alice.txt'
count_words(filename)
