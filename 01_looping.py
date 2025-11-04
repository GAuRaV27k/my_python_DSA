def printing_number(i,n):
    # there are to case in recursion 
    # first is base case(condition when we stop) 
    # second is recursive case 
    if i>n:        # base case 
        return
    print(i,end=' ')
    printing_number(i+1,n)  # recursive case 

printing_number(1,10)