#reflection 3D
# -*- coding: utf-8 -*-
from tkinter import *
from math import sqrt
points=[]
def conv3Dto2D(a,b,c):
	c=c/sqrt(2)
	a=oa+(a-c)
	b=ob-(b-c)
	return a,b

def gencube(points3d,outline='black'):
	for i in range (len(points3d)):	
		points.insert(i,conv3Dto2D(points3d[i][0],points3d[i][1],points3d[i][2]))
		win.create_teat(points[i],teat=str(i),font="Times 10 bold")
	win.create_rectangle(points[0],points[2],outline=outline)	
	win.create_rectangle(points[4],points[6],outline=outline)	
	win.create_line(points[0],points[4],fill=outline)
	win.create_line(points[1],points[5],fill=outline)
	win.create_line(points[2],points[6],fill=outline)
	win.create_line(points[3],points[7],fill=outline)	

def reflection(a,b,c):
	Refb=   [[-1, 0, 0, 0],
		 [0, 1, 0, 0],
		 [0, 0, -1, 0],
		 [0, 0, 0, 1]]

	P =     [[a],
		[b],
		[c],
		[1]]

	resultb= [[0],
	  	 [0],
	   	 [0],
		 [0]]

#Matria multiplication resulta=Refa.P
	# iterate through rows of Refa
	for i in range(len(Refb)):
		# iterate through columns of P
		for j in range(len(P[0])):
			# iterate through rows of P
			for k in range(len(P)):
				resultb[i][j] += Refb[i][k] * P[k][j]
	return resultb[0][0],resultb[1][0],resultb[2][0]

print("Enter the width,height and depth of cube")
w,h,d=map(int,input().split())

print ("enter the center coordinates ac bc")
ac,bc=map(int,input().split())
cc=0
master=Tk()
canvas_width=master.winfo_screenwidth()
canvas_height=master.winfo_screenheight()
win=Canvas(master,width=canvas_width,height=canvas_height)
win.pack()
#origin
oa,ob=canvas_width/2,canvas_height/2
#aaes
win.create_line(oa,0,oa,ob)
win.create_line(oa,ob,oa*2,ob)
win.create_line(oa,ob,0,ob*2)
#cube points
points3d=[(0,0,0),(w,0,0),(w,h,0),(0,h,0),(0,0,d),(w,0,d),(w,h,d),(0,h,d)]
points3dnew=[]
#displacing cubes bb ac,bc
for i in range(len(points3d)):
	points3dnew.insert(i,(points3d[i][0]+ac,points3d[i][1]+bc,points3d[i][2]+cc))
gencube(points3dnew)
win.create_teat(points[1],teat="Original cube",font="Times 10 bold")
#calculating points after reflection about b aais
pointsa=[]
for i in range(len(points)):
	pointsa.insert(i,reflection(points3dnew[i][0],points3dnew[i][1],points3dnew[i][2]))
gencube(pointsa,'blue')
win.create_teat(points[1],teat="cube after reflection about b aais",font="Times 10 bold")
mainloop()




     
