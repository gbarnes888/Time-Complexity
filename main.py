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
    n = len(list)
    if n > 1:
        mid = n // 2
        Left = list[:mid]
        Right = list[mid:]
        mergeSort(Left)
        mergeSort(Right)

        x = 0
        y = 0
        i = 0
        while x < len(Left) and y < len(Right):
            if Left[x] > Right[y]:
                list[i] = Right[y]
                y = y + 1
            else:
                list[i] = Left[x]
                x = x + 1
            i = i + 1
        while x < len(Left):
            list[i] = Left[x]
            x = x + 1
            i = i + 1
        while y < len(Right):
            list[i] = Right[y]
            y = y + 1
            i = i + 1

def heapSort(list):
    length = len(list)
    for x in range((length//2)-1,-1,-1):
        heapify(list,x,length)
    for x in range(length-1,0,-1):
        temp = list[0]
        list[0] = list[x]
        list[x] = temp
        heapify(list,0,x)

def heapify(list, root, length):
    largest = root
    left = (2*root)+1
    right = (2*root)+2

    if left < length and list[left] > list[largest]:
        largest = left
    if right < length and list[right] > list[largest]:
        largest = right

    if largest != root:
        temp = list[largest]
        list[largest] = list[root]
        list[root] = temp
        heapify(list,largest,length)

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
print("Good Test value is 1000000 (1 million)")
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
# bubbleSort(bubblesortlist)
End = time.time()
bubbleSort_runtime = End - Start

 #Insertion Sort
Start = time.time()
# insertionSort(insertionsortlist)
End = time.time()
insertionSort_runtime = End - Start

 #heap Sort
Start = time.time()
heapSort(heapsortlist)
End = time.time()
heapsort_runtime = End - Start

 #merge Sort
Start = time.time()
mergeSort(mergesortlist)
End = time.time()
mergesort_runtime = End - Start

 #print output
print("Bubble Sort Runtime: " + str(bubbleSort_runtime) + " Seconds")
print("insertion Sort Runtime: " + str(insertionSort_runtime) + " Seconds")
print("heap Sort Runtime: " + str(heapsort_runtime) + " Seconds")
print("Merge Sort Runtime: " + str(mergesort_runtime) + " Seconds")

# print(masterList)
# print(bubblesortlist)
# print(mergesortlist)
