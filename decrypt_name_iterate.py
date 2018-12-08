# A program to iterate through all permutations of possible unique integers to 
# try and solve DONALD + GERALD = ROBERT.

from itertools import permutations
import random

i = 0
num_list = [0,1,2,3,4,6,7,8,9]
lett_list = ['T','R','E','B','O','L','A','G','N']
random.shuffle(lett_list)

for perm in permutations(num_list, 9):
    # Given information
    D = 5

    # Construct a dictionary to store unique integers corresponding to letters.
    # Even though I can quickly tell that 'T' should be 0 (and would be best to
    # be listed first), I chose a random ordering of letters to 'not cheat'.
    lett_dict = {
                    lett_list[0]: perm[0],
                    lett_list[1]: perm[1],
                    lett_list[2]: perm[2],
                    lett_list[3]: perm[3],
                    lett_list[4]: perm[4],
                    lett_list[5]: perm[5],
                    lett_list[6]: perm[6],
                    lett_list[7]: perm[7],
                    lett_list[8]: perm[8],
                }
            
    lett_dict['D'] = D
    
    # Convert names to a list of integers.
    donald = [ lett_dict['D'], lett_dict['O'], lett_dict['N'], lett_dict['A'], 
                    lett_dict['L'], lett_dict['D'] ]
    gerald = [ lett_dict['G'], lett_dict['E'], lett_dict['R'], lett_dict['A'], 
                    lett_dict['L'], lett_dict['D'] ]
    robert = [ lett_dict['R'], lett_dict['O'], lett_dict['B'], lett_dict['E'], 
                    lett_dict['R'], lett_dict['T'] ]

    # Convert list of numbers into an integer that can be added.
    donald = int(''.join(map(str,donald)))
    gerald = int(''.join(map(str,gerald)))
    robert = int(''.join(map(str,robert)))
    
    # Check if name assignment satisfies problem and update search progress.
    if i % 50000 == 0:
        print(i)
    
    if (donald + gerald == robert):
        print("\nIt took " + str(i) + " attempts to assign the letters as:")
        print(lett_dict)
        break
    else:
        i += 1



