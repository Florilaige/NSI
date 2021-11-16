from sys import setrecursionlimit
setrecursionlimit(1000)

def fibo(n):
    if n<=1: # Condition d'arrêt
        return 1
    return fibo(n-1)+fibo(n-2)

# Ackermann
def A(m,n):
    if m==0:
        return n+1
    elif m>0 and n==0:
        return A(m-1,1)
    elif m>0 and n>0:
        return A(m-1,A(m,n-1))

'''Ces appels demandent trop d'appels récursifs
print(A(3,3))
print(A(3,4))
print(A(4,1))
print(A(4,2))'''
