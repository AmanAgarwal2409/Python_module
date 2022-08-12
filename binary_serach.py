def binary_search(array, l , h ,k):
    
    
    if  h >= l:
        mid = (h+l)//2
        
        
        if array[mid]==k:
            return mid
            
        elif array[mid] > k:
            return binary_search (array , l, mid-1 , k)
            
        else:
            return binary_search (array , mid+1 , h , k)
            
            
    else:
        return-1
        
array =  [1,2,4,6,8,13,91]
k = 13

result = binary_search(array, 0, len(array)-1, k)
print(result)
