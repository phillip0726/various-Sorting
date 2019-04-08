import random
import csv
from tqdm import tqdm_notebook
import time
import datetime

rand_num = 20000     # 생성할 난수의 개수 : 2만개 
arr = []             # 생성된 난수가 저장되어있는 리스

### 각 정렬방법의 시작시간과 끝나는 시간
startTime = []
endTime = []



def checkTime(func):
    import time
    def newFunc(*args, **kwargs):
        global startTime
        global endTime
        
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        
        startTime.append(start)
        endTime.append(end)
        
    return newFunc


    
'''
    argument    : x   -> 숫자가 저장되어 있는 리스트
                  i,j -> i,j 인덱스
    performence : x[i], x[j]를 swap 한다.
    return      : NULL
'''
def swap(x, i, j):
    x[i], x[j] = x[j], x[i]

'''
    argument    : string -> 파일 이름   ex) "string".txt
                  x      -> 숫자가 저장되어 있는 리스트
    performence : "string".txt 파일을 만들고 리스트 x의 원소들을 파일에 입력한다.
    return      : NULL
'''
def write_file(string, x):
    
    f = open(string+".txt","w")

    print(f"Making {string} file!")
    for i in tqdm_notebook(x):
        f.write(str(i)+"\n")
    print(f"Finish making {string} file!\n")
    f.close()

'''
    argument    : x -> 숫자가 저장되어 있는 리스트
    performence : x를 bubble sort기법을 사용하여 오름차순 정렬함.
    return      : NULL
'''
@checkTime
def bubbleSort(x):
    print("Start Bubble Sort!")

    for size in tqdm_notebook(reversed(range(len(x)))):
        for i in range(size):
            if x[i] > x[i+1]:
                swap(x,i,i+1)
   
    print("Finish Bubble Sort!\n")
    
    write_file("result_bubble",x)
    
'''
    argument    : x -> 숫자가 저장되어 있는 리스트
    performence : x를 selection sort기법을 사용하여 오름차순 정렬함.
    return      : NULL
'''
@checkTime
def selectionSort(x):
    print("Start Selection Sort!")

    for size in tqdm_notebook(reversed(range(len(x)))):
        max_i = 0
        for i in range(1, 1+size):
            if x[i] > x[max_i]:
                max_i = i
        swap(x, max_i, size)

    print("Finish Selection Sort!\n")
    
    write_file("result_selection", x)
    
'''
    argument    : x -> 숫자가 저장되어 있는 리스트
    performence : x를 insertion sort기법을 사용하여 오름차순 정렬함.
    return      : NULL
'''
@checkTime
def insertionSort(x):
    print("Start Insertion Sort!")
  
    for size in tqdm_notebook(range(1, len(x))):
        val = x[size]
        i = size
        while i > 0 and x[i-1] > val:
            x[i] = x[i-1]
            i -= 1
        x[i] = val

    print("Finish Insertion Sort!\n")

    write_file("result_insertion",x)

'''
    argument    : x -> 숫자가 저장되어 있는 리스트
    performence : x를 merge sort기법을 사용하여 오름차순 정렬함.
    return      : NULL
'''
def mergeRecusive(x):
    if len(x) > 1:
        mid = len(x)//2
        lx, rx = x[:mid], x[mid:]
        mergeRecusive(lx)
        mergeRecusive(rx)

        li, ri, i = 0, 0, 0
        while li < len(lx) and ri < len(rx):
            if lx[li] < rx[ri]:
                x[i] = lx[li]
                li += 1
            else:
                x[i] = rx[ri]
                ri += 1
            i += 1
        x[i:] = lx[li:] if li != len(lx) else rx[ri:]
        
'''
    argument    : x -> 숫자가 저장되어 있는 리스트
    performence : mergeRecusive 함수를 호출하고 그 시간을 측정함.
    return      : NULL
'''
@checkTime
def mergeSort(x):
    print("Start Merge Sort!")
    
    mergeRecusive(x)

    print("Finish Merge Sort!\n")
    write_file("result_merge",x)

    
def pivotFirst(x, lmark, rmark):
    pivot_val = x[lmark]
    pivot_idx = lmark
    while lmark <= rmark:
        while lmark <= rmark and x[lmark] <= pivot_val:
            lmark += 1
        while lmark <= rmark and x[rmark] >= pivot_val:
            rmark -= 1
        if lmark <= rmark:
            swap(x, lmark, rmark)
            lmark += 1
            rmark -= 1
    swap(x, pivot_idx, rmark)
    return rmark

'''
    argument    : x -> 숫자가 저장되어 있는 리스트
    performence : x를 quick sort기법을 사용하여 오름차순 정렬함.
    return      : NULL
'''

@checkTime
def quickSort(x, pivotMethod=pivotFirst):
    def _qsort(x, first, last):
        if first < last:
            splitpoint = pivotMethod(x, first, last)
            _qsort(x, first, splitpoint-1)
            _qsort(x, splitpoint+1, last)

    print("Start Quick Sort!")
    
    _qsort(x, 0, len(x)-1)
    
    print("Finish Quick Sort!\n")    

    write_file("result_quick",x)

'''
    argument    : NULL
    performence : 처음 arr에 1,2,...,rand_num 을 저장하고 무작위로 shuffle한다. 바뀐 arr를 rand_100.txt 파일에 입력한다.
    return      : NULL
'''    
def random_million():
    global arr
    
    f = open("rand_100.txt","w")

    arr = [i for i in range(1,rand_num+1)]
    random.shuffle(arr)
    print("Making Input file!")
    for i in tqdm_notebook(arr):
        f.write(str(i)+"\n")
    print("Finish making input file!\n")
    
    f.close()


if __name__ == '__main__':


    #난수 파일 생성
    random_million()

    
    tmp = arr[:]
    bubbleSort(tmp)

    print("=========================================")


    tmp = arr[:]
    selectionSort(tmp)
    

    print("=========================================")


     
    tmp = arr[:]
    insertionSort(tmp)


    print("=========================================")

    tmp = arr[:]
    mergeSort(tmp)
    

    print("=========================================")


    
    tmp = arr[:]
    quickSort(tmp)


    print("============Time Performance===========")
    print(f"Bubble Sort    : %.3f sec"%(endTime[0]-startTime[0]))
    print(f"Selection Sort : %.3f sec"%(endTime[1]-startTime[1]))
    print(f"Insertion Sort : %.3f sec"%(endTime[2]-startTime[2]))
    print(f"Merge Sort     : %.3f sec"%(endTime[3]-startTime[3]))    
    print(f"Quick Sort     : %.3f sec"%(endTime[4]-startTime[4]))    
