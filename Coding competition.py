import numpy as np
t = int(input('enter number of test cases: '))
#we should declare an empty dictionary for its usage
myDict = {}
yes = 0
no = 0
for i in range(t):
    #in every iteration of for i range of t we get n,q
    n = int(input('enter number of teams: '))
    q = int(input('enter number of J and ? s: '))
    myMatrix = np.zeros((n,n))
    for i in range(q):
        JOrQue,X,Y = input("entre input: ").split()
        #here we decide if our first character is J or ?
        if JOrQue == 'J': 
            myMatrix[int(X)-1,int(Y)-1] = 1
            myMatrix[int(Y)-1,int(X)-1] = 1
            #we should update our matrix to make tansitive relation work
            myMatrix = myMatrix+np.dot(myMatrix,myMatrix)
        else:
            if myMatrix[int(X)-1,int(Y)-1] != 0:
                yes += 1
            else:
                no += 1
    #we append yes numbers as key and no numbers as value
    myDict[i] = [yes,no]
    yes = 0
    no = 0
for i in myDict:
    print('yes:',myDict[i][0],'no:',myDict[i][1])
             
