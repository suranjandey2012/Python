import matplotlib.pyplot as plt
import numpy as np
import math as m
import random as r

#List to store all the points
Points=[]


#Function computes the distance between 2 points
def computedistance(P1,P2):
   return (m.sqrt(pow(P2[0]-P1[0],2)+pow(P2[1]-P1[1],2)))



# Function returns midpoint of line connecting 2 points
def findmidpoint(P1,P2):
   return ((P1[0]+P2[0])/2,(P1[1]+P2[1])/2)


#Function to find the center using 3 points
def find_center_3_Points(A, B, C):
   try:
      g = (-1) * ((A[0] ** 2 + A[1] ** 2) * (C[1] - B[1]) + (B[0] ** 2 + B[1] ** 2) * (A[1] - C[1]) + (
                 C[0] ** 2 + C[1] ** 2) * (B[1] - A[1])) / (
                     2 * (A[0] * (B[1] - C[1]) - A[1] * (B[0] - C[0]) + (B[0] * C[1]) - (C[0] * B[1])))
      f = (-1) * ((A[0] ** 2 + A[1] ** 2) * (B[0] - C[0]) + (B[0] ** 2 + B[1] ** 2) * (C[0] - A[0]) + (
                 C[0] ** 2 + C[1] ** 2) * (A[0] - B[0])) / (
                     2 * (A[0] * (B[1] - C[1]) - A[1] * (B[0] - C[0]) + (B[0] * C[1]) - (C[0] * B[1])))
   except ZeroDivisionError:
      return (10 ** 18, 10 ** 18)
   center = (g, f)
   return center

#Method to Check if the New Circle is enclosing all other points
def IS_Enclosing(Points,center,radius):
   for P in Points:
      if(computedistance(P,center)>radius):
         return False
   return True


#Draw the singleton points on the 2D plain
def drawsingletoncircles(Points):
   P=np.array(Points)
   x,y=P.T
   plt.scatter(x,y,color="Red")



#Draw the circles considering the 2 points as diametric endpoints
def draw2pointcircle(Points):
   circles=[]
   for i in range(len(Points)):
      for j in range(i+1,len(Points)):
         center=findmidpoint(Points[i],Points[j])
         #print(Points[i],Points[j],center)
         radius=computedistance(center,Points[i])
         #print(Points[i],Points[j],center,radius)
         circles.append((center,radius))
   return circles


#Function to compute the Min Enclosing Circle
def CalculateMinEnclosingCircle(Points):
   #Get the max x coordinate
   '''Max_x=-1
   for P in Points:
      if(P[0]>Max_x):
         Max_x=P[0]'''

   final_radius=10**18
   final_center=None

   #Check for all 2 points Min Circle
   for i in range(len(Points)):
      for j in range(i+1,len(Points)):
         center=findmidpoint(Points[i],Points[j])
         radius=computedistance(center,Points[i])

         #print("Inside Function", center, radius)

         if(radius<final_radius and IS_Enclosing(Points,center,radius)):
            final_radius=radius
            final_center=center

   #Check for all 3 points:
   for i in range(len(Points)):
      for j in range(i+1,len(Points)):
         for k in range(j+1,len(Points)):
            center=find_center_3_Points(Points[i],Points[j],Points[k])
            radius=computedistance(center,Points[i])
            #print("Inside Function", center, radius)

            if (radius < final_radius and IS_Enclosing(Points, center, radius)):
               final_radius = radius
               final_center = center

   return (final_center,final_radius)



#Input
N=int(input("Enter the number of points:"))


#main
for i in range(N):
   #point=tuple(map(int,input().split()))
   point=(r.randint(-100,100),r.randint(-100,100))
   Points.append(point)

#print X-Y Axis
plt.axline((0,0),slope=0,color='b')
plt.axline((0,0),(0,1),color='b')
plt.xlabel("X axis")
plt.ylabel("Y axis")

#print(Points)
drawsingletoncircles(Points)

#print(2 point Min Circles)
listcircle2=draw2pointcircle(Points)


#Function call to get the min enclosing circle using Brute Force approach
Point3=CalculateMinEnclosingCircle(Points)

print("Center and Radius of the minenclosing circle are:",Point3)

print("The points are:",Points)


#figure,axes = plt.subplots()

for c in listcircle2:
   drawcircle=plt.Circle(c[0],radius=c[1],fill=False)
   plt.gca().add_artist(drawcircle)  #getcurrent axis

#Plot The Min Enclosing Circle
drawmincircle=plt.Circle(Point3[0],radius=Point3[1],fill=False,edgecolor="Yellow")
plt.gca().add_artist(drawmincircle)  #getcurrent axis

#Plot The Center Of The Min Enclosing Circle
plt.scatter(Point3[0][0],Point3[0][1],color="Green")

plt.show()