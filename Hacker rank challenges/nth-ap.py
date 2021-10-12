'''Given a series 9, 33, 73, 129... Find the n-th term of the series.

Input Format

4

Constraints

Nil

Output Format

129

Sample Input 0

4
Sample Output 0

129
Explanation 0

4th term of the series is 129.'''

        #----->>    doubt  

n=4
l=[9,33,73]
for i in range(3,n):
    if i%2!=0:
        k=l[(i//2)-1]*10+2
        print(k)
    else:    
        k=l[i//2]*10+1
        print(k)        