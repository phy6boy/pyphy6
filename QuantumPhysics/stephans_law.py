'''
This program is used to find the values for stefans law
args:
    temperature or T : find the Energy
    Energy or E : find the temperature
'''

import sys

sigma = 5.67e-8

def compute_energy(T):
	return T**4*sigma

def compte_temp(E):
	return (E/sigma)**(1/4)


if __name__=='__main__':
	args = sys.argv

	if len(args)>1:
	    if args[1]=='T' or args[1].upper()=='TEMPERATURE':
	        T = float(args[2])
	        E = T**4*sigma
	        print('Enerrgy per unit time per unit area (radiancy): ',E)
	    elif args[1].upper() == 'E' or args[1].upper()=='ENERGY':
	        E = float(args[2])
	        T = (E/sigma)**(1/4)
	        print('Temperature: ',T)
	    else:
	        print('Not a valid argument. please refer to script')
	else:
	    print('No arguments')

