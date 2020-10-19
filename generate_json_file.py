import json
import random

number_of_lines = 1000000
number_of_cols = 300
structure = {'Column : {}'.format(str(i)):int(random.random()*100) for i in range(number_of_cols)}

with open('generated_file.txt', 'w') as wf:
	for rown in range(number_of_lines):
		if (rown % 20000 == 0) and (rown > 1):
			answer=input('Mais 20k linhas escritas, continuar? (False para não) \n')
			if (answer == 'False'):
				break
		wf.write(json.dumps(structure) + '\n')
