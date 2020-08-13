"""
Problem Statement
Paste your text here : you are given an integer ​n​ denoting an ​nxn​ matrix.
Initially, each cell of the matrix is empty. You are given ​k​ tasks.
In each task, you are given a cell ​(i,j)​ where the cell ​(i,j)​ represents the ​i row and
​j​ column of the given matrix. You have to perform each task sequentially in the given order.
Each task is described in a cell ​(i,j)​. For each task, you have to place ​x ​in each cell
of row and each cell column . After you complete each task, you are required to print the number of empty
cells in the matrix. Input format:  1. The first line contains two space-separated integers n and k​
where ​n​ is the number of rows and columns in the given matrix and ​k​ is the number of
 tasks respectively. 2. Next ​k​ lines contain two space-separated integers. Output format: print
  ​k​ space-separated integers denoting the number of empty cells in the matrix. )


"""

#Solution
N = int(input())
K = int(input())

X = set()
Y = set()
for i in range(K):
    x,y = list(map(int,input().split()))
    X.add(x)
    Y.add(y)
print(X)
print(Y)
for i in range(N):
    for j in range(N):
        if i not in X and j not in Y:
            print(" {},{} ".format(i,j),end='')
        else:
            print("  .  ",end='')
    print()

"""
output tested
{1, 6}
{1, 3, 5}
 0,0   .   0,2   .   0,4   .   0,6  0,7 
  .    .    .    .    .    .    .    .  
 2,0   .   2,2   .   2,4   .   2,6  2,7 
 3,0   .   3,2   .   3,4   .   3,6  3,7 
 4,0   .   4,2   .   4,4   .   4,6  4,7 
 5,0   .   5,2   .   5,4   .   5,6  5,7 
  .    .    .    .    .    .    .    .  
 7,0   .   7,2   .   7,4   .   7,6  7,7

For this input 8
3
1 1
1 5
6 3
"""