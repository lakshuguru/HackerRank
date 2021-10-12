'''Given a linked list and two integers M and N. Traverse the linked list such that you retain M nodes then delete next N nodes, continue the same until end of the linked list.

Input Format

M = 2 N = 2 Linked List: 1->2->3->4->5->6->7->8

Constraints

Nil

Output Format

1->2->5->6

Sample Input 0

2
2
1 2 3 4 5 6 7 8
Sample Output 0

1 2 5 6
Explanation 0

Nil'''
m=int(input())
n=int(input())
#l=list(map(int,input().split()))
l=[1,2,3,4,5,6,7,8,9,10]
i=0
k=0
while i<len(l):
    print(l[k],l[k+1],end=' ')
    k+=2
    for j in range(n):
        l.pop(n)      
    i+=2
