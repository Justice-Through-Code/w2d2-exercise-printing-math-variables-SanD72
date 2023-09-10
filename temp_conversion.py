
def convert_100_to_celsius():
    celsius_100 = (100 - 32) * (5 / 9)
    print(f'{celsius_100}')
    print('float') 

#I know the result will be a float because division was among the operatios in the equation
   
convert_100_to_celsius()

def convert_0_to_celsius():
    celsius_0 = (0 - 32) * (5 / 9)
    print(celsius_0)
    # Convert a temperature of 0 degrees fahrenheit to celsius
    # Save this to a variable called celsius_0, and use print() to print out the value

convert_0_to_celsius()

def convert_34_2_to_celsius():
   # convert_34_2_to_celsius = (34.2 - 32) * 5 / 9
#print('convert_34_2_to_celsius')
    # Convert a temperature of 34.2 degrees fahrenheit to celsius
    # Do this one all in one print statement without saving any variables
    
    print((34.2 - 32) * 5 / 9)
convert_34_2_to_celsius()

# Now, can you convert back?
print('(-0.999 * 9/5) + 32')


def convert_5_to_fahrenheit():
    print(5 * (9 / 5) + 32)

convert_5_to_fahrenheit()

def hotter_temp():
    comp_celsius = (30.2 * (9/5) + 32)
    if comp_celsius > 85.1:
        print('30.2 degrees celsius')
    elif comp_celsius < 85.1:
        print('85.1 degrees fahreheit')

    # What is hotter, a temperature of 30.2 degrees celsius, or a temperature of 85.1 degrees fahrenheit?
    # Print out the hotter temp: '30.2 degrees celsius' or '85.1 degrees fahrenheit', respectively

hotter_temp()