import random
import sys
import time



sort = []


for i in range(100):
	sort.append(random.randint(1, 9))




def sort_index(array, index):
	l = array
	x = l[index]
	y = l[index+1]

	if x > y:
		l[index] = y
		l[index+1] = x

	return l



def chack_for_finish(array):
	l = array
	cq = 0
	count = 1
	for i in range(len(l)-1):
		if l[cq] > l[count]:
			return False

		count += 1
		cq += 1



def listToString(s):  
    
    # initialize an empty string 
    str1 = ""  
    
    # traverse in the string   
    for ele in s:  
        str1 += str(ele)   
    
    # return string   
    return str1  







print(listToString(sort), '\n\n')

t = time.time()



while True:
	
	
	for i in range(len(sort)-1):
		sort = sort_index(sort, i)
		s = listToString(sort)
			
	
		sys.stdout.write('\r'+s)
		#time.sleep(0.01)

	if sort == sorted(sort):
		break

		

print('\ndone in:', str(time.time()-t), 'seconds')

