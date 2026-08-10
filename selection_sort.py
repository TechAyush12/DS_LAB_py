arr = [] #List of elements
n = int(input("Enter the numbers of elements :- "))
for i in range( 1 ,n + 1 ):
    inp = int(input(f"Enter salary of employee {i} :- "))
    arr.append(inp)
print(arr) #user entered list\

def selection(arr):
    l = len(arr)
    for i in range(l):
        low = i
        for j in range(i+1 , l):
            if(arr[j] < arr[low]):
                low = j
        arr[low] , arr[i] =  arr[i] , arr[low]
    return arr

print("The sorted list :- " , selection(arr))

#printing highest salary
top_five = []
for i in range(-1 , -6 , -1):
    top_five.append(arr[i])
    
    