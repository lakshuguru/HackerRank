'''Given an array Arr of N positive integers. Your task is to find the elements whose value is equal to that of its index value.

Input Format

5 15 2 45 12 7

Constraints

Nil

Output Format

2

Sample Input 0

5
15 2 45 12 7
Sample Output 0

2
Explanation 0

Only Arr[2] = 2 exists here.'''

n=int(input())
p=list(map(int,input().split()))
print(p)    
for i in range(1,n+1):    
    if i==p[i-1]:
        print(p[i-1])