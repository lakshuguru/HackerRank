'''You are given an array A of size N. You need to print elements of A in alternate order (starting from index 0).

Input Format

4 1 2 3 4

Constraints

Nil

Output Format

1 3

Sample Input 0

4
1 2 3 4
Sample Output 0

1 3 
Explanation 0

Nil'''

n=int(input())
l=list(map(int,input().split()))
for i in range(0,n,2):
    print(l[i],end=' ')