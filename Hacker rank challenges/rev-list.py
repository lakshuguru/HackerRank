'''Given an array A of size N, print the reverse of it.

Input Format

1 4 1 2 3 4

Constraints

Nil

Output Format

4 3 2 1

Sample Input 0

1
4
1 2 3 4
Sample Output 0

4 3 2 1'''
# n=int(input())
# t=int(input())
l=list(map(int,input().split()))
#l=[1,2,3,4]
for i in range(len(l),0,-1):
    print(i,end=' ')