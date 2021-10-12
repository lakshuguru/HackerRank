'''Given a positive integer n. Find the sum of product of x and y such that floor(n/x) = y .

Input Format

5

Constraints

Nil

Output Format

21

Sample Input 0

5
Sample Output 0

21
Explanation 0

Following are the possible pairs of (x, y): (1, 5), (2, 2), (3, 1), (4, 1), (5, 1). So, 1*5 + 2*2 + 3*1 + 4*1 + 5*1 = 5 + 4 + 3 + 4 + 5 = 21.'''
n=int(input())
a=0
y=1
for i in range(1,n+1):
    y=int(n/i)
    a+=(y*i)
print(a)