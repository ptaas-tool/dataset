import random
import json
import glob
import os
import sys


# find the number of file
list_of_files = glob.glob('./backup/*.json')
if len(list_of_files) == 0:
    list_of_files.append("/backup/data.000.json")

latest_file = max(list_of_files, key=os.path.basename)
number = int(latest_file.split('/')[2].split('.')[1])


# const variables
VULNERABILITIES_PATH = "./docs/vulnerabilities.txt"
ATTACKS_PATH = "./docs/attacks.txt"
OUTPUT_PATH = f"./backup/data.{number+1:03d}.json"
BATCHES = int(sys.argv[1])
MAX_RAND = int(sys.argv[2])


# base lists
vulnerabilities = []
attacks = []


# read input documents
with open(VULNERABILITIES_PATH, 'r', encoding='UTF-8') as file:
    while line := file.readline():
        vulnerabilities.append(line.rstrip())

with open(ATTACKS_PATH, 'r', encoding='UTF-8') as file:
    while line := file.readline():
        attacks.append(line.rstrip())

print(f'[INFO] loaded {len(attacks)} attacks, {len(vulnerabilities)} vulnerabilities into system.')

if __name__ == "__main__":
    # generate output data list
    outputs = []
    
    print(f'Output file is "{OUTPUT_PATH}"\n\n')

    try:
        # creating 100 attacks
        for i in range(0, BATCHES):
            # get random vulnerabilities
            v_tmp = random.randint(1, MAX_RAND)
            v_list = random.sample(vulnerabilities, k=v_tmp)
            
            print()
            print(f'batch {i+1} out of {BATCHES}')
            print("=======")
            print()

            print(" | ".join(v_list))
            
            print() 
            print("=======")
            print()

            # select attacks
            for index, item in enumerate(attacks):
                if index == len(attacks) - 1:
                    print(f'[{index}] {item}')
                else:
                    print(f'[{index}] {item}', end=", ")
            
            print()
            print()
            selected = input('> select attacks: ').split(',')
            
            # generate output
            outputs.append({
                'vulnerabilities': v_list,
                'attacks': [attacks[int(j)] for j in selected]
            })
            
            print()
            
        # save output
        with open(OUTPUT_PATH, 'w') as file:
            file.write(json.dumps(outputs, indent=4))
    except KeyboardInterrupt:
        print('terminated ...')
        # save output
        with open(OUTPUT_PATH, 'w') as file:
            file.write(json.dumps(outputs, indent=4))
