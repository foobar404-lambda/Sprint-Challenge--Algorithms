#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a)
O(n)
the loop will break after n iterations


b)
O(n^2)
because of the nested loops, although because j jumps by multiples of 2, O(nlogn) sounds close, but that is usually reserved for sorting 

c)
O(n)
the function will loop n amount of times 

## Exercise II


## solution 1
drop one egg per floor 
stop when first egg brakes 
worst case: O(n)

## solution 2

start at middle floor
if egg brakes, current floor is the new top floor, find the new middle floor
if egg doesint brake, current floor is the new lowest floor, find the new middle
drop egg until two floors are found
return floor that egg does not brake on 
worst case: O(log(n))


