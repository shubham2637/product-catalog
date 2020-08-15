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
c=0
for i in range(K):
    x,y = list(map(int,input().split()))
    X.add(x)
    Y.add(y)
#print(X)
#print(Y)
for i in range(N):
    for j in range(N):
        if i not in X and j not in Y:
            c+=1
print(c)

