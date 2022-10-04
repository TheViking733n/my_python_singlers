"""
@Author: The Viking
@Date: 13 Jan, 2022
@Description:
 *  My single liner codes for Pascal's Triangle

 *  I call a code single liner if its written in one line without using exec() or ;

 *  Also, this code for code Pascal Triangle will increase padding between numbers
    automatically with increase in n

"""

(lambda n:print(*[(' '*((i%2)*(max(4,n//3+1)//2)+max(4,n//3+1)*((n-i+n%2)//2))+''.join([f"{(lambda n,r:eval(f'{str(tuple(range(n-r+1,n+1)))}//{str(tuple(range(1,r+1)))}'.replace(',','*').replace('*)',')')) if n-r>0 and r>0 else 1)(i,r)}".center(max(4,n//3+1)) for r in range(i+1)])) for i in range(n+1)],sep='\n'))(int(input('Enter no. of rows of Pascal Triangle you want to generate: '))-1)
