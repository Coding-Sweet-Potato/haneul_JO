def closestNumbers(arr):
    output = []
    arr = sorted(arr)
    Nmin = 10**9
    
    for ind in range(1, len(arr)):
        diff = abs(arr[ind-1] - arr[ind])
        
        if diff < Nmin:
            output = [(arr[ind-1], arr[ind])]
            Nmin = diff
        elif diff == Nmin:
            output.append((arr[ind-1], arr[ind]))
            
    flat_list = [item for sublist in output for item in sublist]
        
    return flat_list
    

if __name__ == "__main__":
    n = int(input().strip())
    arr = list(map(int, input().strip().split(' ')))
    result = closestNumbers(arr)
    print (" ".join(map(str, result)))
