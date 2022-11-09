'''Geek left with no food:

geek has N food items.Every second geek will eat:

 i)N/2 foods items if N is divisible by 2
 ii)(N+1)/2 food items if N is not divisible by 2.
Find the time at which no food is left with geek.

Example 1:
Input:
N=4
Output:
3
Explanation:
In First second geek will eat (4/2) item after that 
food item left will be 2. In 2nd second geek will eat 
(2/2) item so food item left will be 1.In 2nd 
second geek will eat ((1+1)/2) item so food item 
left will be 0.
Example 2:
Input:
N=0
Output:
0
Explanation:
There is no food items to eat.
'''



def minimumCost(n,x):
    coin=0
    center=n//2
    for i in range(0,n):
        if(i<center):
            val=x[center]-x[i]
            if(val%2!=0):
                coin+=1
        elif(i==center):
            continue
        else:
            sums=x[i]-x[center]
            if(val%2!=0):
                coin+=1
    return coin
    
print(minimumCost(3,[2,4,6]))