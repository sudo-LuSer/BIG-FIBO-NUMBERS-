NMAX = (10**7)+1
FiboIdentity = [[1,1],
				[1,0]]
FIBO = [FiboIdentity]
def MultiPly2D(A,B):
	AB = [
	[(A[0][0]*B[0][0]) + (A[0][1]*B[0][1]) , (A[0][0]*B[0][1]) + (A[0][1]*B[1][1])]
	,[(A[1][0]*B[0][0]) + (A[1][1]*B[1][0]) , (A[1][0]*B[0][1]) + (A[1][1]*B[1][1])]
	]
	return AB 
def pleinFIBO(FIBO):
	for i in range(1,NMAX):
		FIBO.append(MultiPly2D(FIBO[i-1],FiboIdentity))
pleinFIBO(FIBO)
print(FIBO[NMAX][1][1])
