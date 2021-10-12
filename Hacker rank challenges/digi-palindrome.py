'''Given a Integer array A[] of n elements. Your task is to complete the function PalinArray. Which will return 1 if all the elements of the Array are palindrome otherwise it will return 0. Input: The first line of input contains an integer denoting the no of test cases. Then T test cases follow. Each test case contains two lines. The first line of input contains an integer n denoting the size of the arrays. In the second line are N space separated values of the array A[]. Output: For each test case in a new line print the required result.

Input Format

1 5 111 222 333 444 555

Constraints

1 <=T<= 50 1 <=n<= 20 1 <=A[]<= 10000

Output Format

1

Sample Input 0

1
5
111 222 333 444 555
Sample Output 0

1
Explanation 0

For First test case. n=5; A[0] = 111 //which is a palindrome number. A[1] = 222 //which is a palindrome number. A[2] = 333 //which is a palindrome number. A[3] = 444 //which is a palindrome number. A[4] = 555 //which is a palindrome number. As all numbers are palindrome so This will return 1.'''
#t=int(input())
n=int(input())
d=0
a=list(map(int,input().split()))
for i in range(len(a)):
    b=a[i]%10
    a[i]=a[i]//10
    c=a[i]%10
    a[i]=a[i]//10
    print(b,a[i],c)
    if(b==c and b==a[i] and c==a[i]):
      d+=1
if d==n:
  print('1')
else:
  print('0')   