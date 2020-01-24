"""
make_insert.py by Cameron Wertelka

A python file to process cars.csv to create SQL insert statements

"""

infile = open('cars.csv', 'r')
infile.readline()
lines = infile.readlines()
#print(lines)

for line in lines:
	line = line.strip()
	tokens = line.split(' ,')
	print("insert into cars(make,model,price) ", end="")
	print("values ('" + tokens[0] + "','" + tokens[1] + "'," + tokens[2] + ");") 
	
infile.close
infile = open('customers.csv', 'r')
infile.readline()
lines = infile.readlines()

for line in lines:
	line = line.strip()
	tokens = line.split(' ,')
	print("insert into customers(first_name,last_name,sex) ", end="")
	print("values ('" + tokens[0] + "','" + tokens[1] + "','" + tokens[2] + "');") 
