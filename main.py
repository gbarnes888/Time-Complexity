import random
import time

 #Function to generate a random list of n values each between 1-100000
def generatelist(n):
    list = []
    for x in range(0,n):
        list.append(random.randint(1,100000))
    return list

 #Function for each sort used
def mergeSort(list):
    # Our Code Here
    return

def heapSort(list):
    # Our Code Here
    return

def quickSort(list):
    # Our Code Here
    return

def bubbleSort(list):
    n = len(list)
    for x in range(0,n):
        for y in range(0, n-1-x):
            if list[y] > list[y+1]:
                temp = list[y]
                list[y] = list[y+1]
                list[y+1] = temp

def insertionSort(list):
    n = len(list)
    for x in range(1,n):
        temp = list[x]
        y = x -1
        while y >= 0 and temp < list[y]:
            list[y+1] = list[y]
            y = y-1
        list[y+1] = temp

def regexSort(list):
    # Our Code Here
    return


 #Gets n as input from user and generates masterList can makes copies for each sort
n = int(input("Enter a value for n for the size of the list to sort:"))
masterList = generatelist(n)
mergesortlist = masterList[:]
heapsortlist = masterList[:]
quicksortlist = masterList[:]
bubblesortlist = masterList[:]
insertionsortlist = masterList[:]
regexsortlist = masterList[:]

 #Run and time sort functions
 #Bubble Sort
Start = time.time()
bubbleSort(bubblesortlist)
End = time.time()
bubbleSort_runtime = End - Start

 #Insertion Sort
Start = time.time()
insertionSort(insertionsortlist)
End = time.time()
insertionSort_runtime = End - Start

 #print output
print("Bubble Sort Runtime: " + str(bubbleSort_runtime) + " Seconds")
print("insertion Sort Runtime: " + str(insertionSort_runtime) + " Seconds")
