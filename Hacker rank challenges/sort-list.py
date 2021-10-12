'''Given a Singly linked list with each node containing either 0, 1 or 2. Write code to sort the list.

Input Format

1 1 2 0 4 3

Constraints

Nil

Output Format

0 1 1 2 3 4

Sample Input 0

1 1 0 2 4 3
Sample Output 0

0 1 1 2 3 4'''
l=list(map(int,input().split()))
p=sorted(l)
s=' '.join([str(i) for i in p])
print(s)    