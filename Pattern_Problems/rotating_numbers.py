(lambda n:print(*[" ".join([str(i) for i in range(1,n+1)][i:]+[str(i) for i in range(1,n+1)][:i]) for i in range(n)],sep="\n"))(int(input("Enter n = ")))
