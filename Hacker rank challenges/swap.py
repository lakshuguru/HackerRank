'''Given an array Arr of size N, swap the Kth element from beginning with Kth element from end.

Input Format

8 3 1 2 3 4 5 6 7 8

Constraints

Nil

Output Format

1 2 6 4 5 3 7 8

Sample Input 0

8
3
1 2 3 4 5 6 7 8
Sample Output 0

1 2 6 4 5 3 7 8
Explanation 0

Kth element from beginning is 3 and from end is 6.'''

t=int(input())
n=int(input())
s=' '
l=list(map(int,input().split())) 
print(l[n-1])
print(l[-n])
k=l[n-1]
l[n-1]=l[-n]
l[-n]=k
print(s.join(map(str,l)))