'''
This program is used to find the values for wien's displacement law
args:
    temperature or T : find the Energy
    Energy or E : find the temperature
'''

import sys

constant = 2.898e-3  #m-K    wiens contant

def compute(variable):
    """compute wavelength if temperature is given or vice versa
    """
    return constant/variable

if __name__=='__main__':
    args = sys.argv

    if len(args)>2:
        if args[1]=='L' or args[1].upper()=='LAMBDA':
            L = float(args[2])
            T = constant/L
            print('Temperature:  ',T)
        elif args[1].upper() == 'T' or args[1].upper()=='TEMPERATURE':
            T = float(args[2])
            L = constant/T
            print('Wavelength of maximum emission: ',L)
        else:
            print('Not a valid argument. please refer to script')
    else:
        print('No: of arguments is invalid for calculation')

