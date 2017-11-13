# This program is a basic unit converter. It implements python dictionary functionality to
# create a simple user interface to convert distances, weights, and liquid volumes.

def convert_units(amt = 0, fro = '', to = '', map = {}):
# Basic function that takes an original amount, the unit-type to convert from, and the unit to convert to.
# For the purposes of this program, the dictionary map representing conversion rates between units is also
# passed to the function.
    mid = ''
    # These flow statements identify which type of unit we will be converting and then setting the mid-step unit
    # to the base unit for that unit-tree. For example, if we want to convert from oz to pound, the second elif is
    # evaluated as true (as 'oz' is found as a key in the sub-dict map['lb']. Then, 'lb' is set to the base unit
    # for an easy 2-step conversion.
    if fro in map['m']: mid = 'm'
    elif fro in map['lb']: mid = 'lb'
    elif fro in map['cup']: mid = 'cup'
    # Basic arithmetic to take the original amount, convert to the base unit, and then convert to the final unit.
    new = amt/map[mid][fro] * map[mid][to]
    return new

# Python dictionary which holds one base unit for each type of conversion. Each of those base units
# hold individual dictionaries which hold the number of the various units convertible to 1 unit of the base unit.
table = {"m": {"m": 1,
             "ft": 3.28084,
             "cm": 100,
             "mm": 1000,
             "mi": 0.000621371,
             "yd": 1.09361,
             "km": .001,
             "in": 39.3701
             },
       "lb": {"lb": 1,
              "mg": 453592,
              "kg": 0.453592,
              "oz": 16,
              "g": 453.592
              },
       "cup": {"cup": 1,
               "floz": 8,
               "qt": .25,
               "mL": 236.588,
               "L": 0.236588,
               "gal": 0.0625,
               "pint": 0.5
               }
       }

print( "Welcome!\n\n",
       "Distances: ft cm mm mi m yd km in\n  Weights: lb mg kg oz g\n  Volumes: floz qt cup mL L gal pint")

# Continuous loop that only stops upon a user-induced break
while True:
    # Creates a list that has parsed our consistently formatted input which is well-defined below.
    inp = input("Convert [AMT SOURCE_UNIT in DEST_UNIT, or (q)uit]: ").split()
    try:
        # Stop condition
        if inp[0] == 'q': print("Thanks for converting with us."); break
        else:
            converted = convert_units(amt = float(inp[0]), fro = inp[1], to = inp[3], map = table)
            print(inp[0], inp[1], "=", converted, inp[3], sep = " ")
    except: print("Input error, please try again.")






