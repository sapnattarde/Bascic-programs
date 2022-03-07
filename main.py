
#print upper triangle
space = 5
for i in range(1,6): # outer loop to count rows
  for k in range(1,space): # loop to leave space
    print(" ", end ="")
  for j in range(1,i+1):   # loop to print "*"
    print("*", end=" ")
  print()
  space-=1

#print lower triangle
space = 2
for i in range(5,1,-1):
  for k in range(1,space):
    print(" ",end="")
  for j in range(1,i):
    print("*", end=" ")
  print() 
  space+=1
  