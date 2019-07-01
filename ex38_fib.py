# znajdz n-ty element ciagu fibonacciego

def recur_fibo(n):  # rozwiazanie rekurencyjne, ostroznie z duzymi liczbami
   if n <= 1:
       return n
   else:
       return(recur_fibo(n-1) + recur_fibo(n-2))

# print(recur_fibo(50))

def fib(n): # rozwiazanie liniowe
    a,b = 1,1
    for i in range(n-1): # 0,1,2,3,4
        a,b = b,a+b
    return a

print fib(1000)
