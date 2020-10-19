import pandas as pd
import json 
import time

start = time.time()
max_lines = 100000
final_list = []
count = 0
with open('generated_file.txt', 'r') as rf:
	lines = rf.readlines()
	for row in lines:
		count+=1
		final_list.append(json.loads(row))
		if (count%10000==0):
			print('Progresso: {}'.format(count/len(lines)))
		if (count >= max_lines):
			print('Finalizando leitura por max_lines')
			break

print(pd.json_normalize(final_list))
elapsed_time = (time.time() - start)
print(elapsed_time)


