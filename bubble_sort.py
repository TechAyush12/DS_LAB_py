arr = [] #List of elements
n = int(input("Enter the numbers of elements :- "))
for i in range( 1 ,n + 1 ):
    inp = int(input(f"Enter salary of employee {i} :- "))
    arr.append(inp)
print(arr) #user entered list

def bubble(arr):
    n = len(arr)
    for i in range(n):
            for j in range(0 , n - 1 - i):
                if(arr[j] > arr[j+1]):
                 arr[j] , arr[j+1] = arr[j+1] , arr[j]
    return arr
print("Sorted list :- ", bubble(arr))

#printing highest salary
top_five = []
for i in range(-1 , -6 , -1):
    top_five.append(arr[i])
print(top_five)
    



   
