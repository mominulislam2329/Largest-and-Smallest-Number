# set the initial condition to None
largest = None
smallest = None
#initiate an indefinite while loop to take numerous inputs
# Boolean expression is used to make an indefinite loop
while True:
    number = input('Enter a number> ')
    if number == 'done' :
        break
    try: # string input should be converted to float/int value
        f_number = float(number)
        if largest is None or largest < f_number:
            largest = f_number
        if smallest is None or smallest > f_number:
            smallest = f_number
    except:
        print('You have entered invalid input')
        continue # will go to the inital loop to excute from the beginning
print("Maximum is", largest)
print("Minimum is", smallest)
