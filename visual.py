import random
import sys
import time
import turtle

wn = turtle.Screen()
wn.setup(2000, 1500)
wn.tracer(0)

draw = turtle.Turtle()


sort = []


for i in range(200):
	sort.append(i)


def scrambled(orig):
    dest = orig[:]
    random.shuffle(dest)
    return dest

sort = scrambled(sort)

def sort_index(array, index):
	l = array
	x = l[index]
	y = l[index+1]

	if x > y:
		l[index] = y
		l[index+1] = x

	return l







def listToString(s):  
    
    # initialize an empty string 
    str1 = ""  
    
    # traverse in the string   
    for ele in s:  
        str1 += str(ele)   
    
    # return string   
    return str1  


def draw_sc(array):
	l = array
	draw.up()
	draw.goto(-950, -700)
	draw.setheading(90)
	draw.down()
	for i in l:
		
		draw.forward(i*7)
		#wn.update()
		
		draw.backward(i*7)
		#wn.update()

		draw.setx(draw.xcor()+9.5)

	wn.update()




def satisfiy_without_delay(array):
	l = array
	draw.up()
	draw.goto(-950, -700)
	draw.setheading(90)
	draw.down()
	draw.color('red')

	for i in l:
		
		draw.forward(i*7)
		#wn.update()
		
		draw.backward(i*7)
		#wn.update()

		draw.setx(draw.xcor()+9.5)
		wn.update()
		


draw.ht()
draw.pensize(10)
draw_sc(sort)

#print(listToString(sort), '\n\n')

t = time.time()
while True:
	for i in range(len(sort)-1):
		sort = sort_index(sort, i)
		s = listToString(sort)
	draw.clear()
	
	#draw.color('black')
	draw_sc(sort)
	
	#draw.clear()
	
	if sort == sorted(sort):
		break



draw.color('black')
draw_sc(sort)
satisfiy_without_delay(sort)

print('done in:', str(time.time()-t), 'seconds')

wn.mainloop()
