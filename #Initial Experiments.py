# Initial Experiments with Wolfram 30
f = "🟨" #full
e = "⬛" #empty
n = 100 #number of iterations
seed = [f] * (n-1)
seed.insert(n//2, e)

def tileprinter(seed, n):
    print(''.join(seed))
    for x in range((n-1)//2):
        old_seed = seed.copy()
        for y in range(1, n-1): 
            if old_seed[y - 1] == e and old_seed[y] == e and old_seed[y + 1] == e:
                seed[y] = f
            elif old_seed[y - 1] == e and old_seed[y] == e and old_seed[y + 1] == f:
                seed[y] = f
            elif old_seed[y - 1] == e and old_seed[y] == f and old_seed[y + 1] == e:
                seed[y] = f
            elif old_seed[y - 1] == e and old_seed[y] == f and old_seed[y + 1] == f:
                seed[y] = e
            elif old_seed[y - 1] == f and old_seed[y] == e and old_seed[y + 1] == e:
                seed[y] = e
            elif old_seed[y - 1] == f and old_seed[y] == e and old_seed[y + 1] == f:
                seed[y] = e
            elif old_seed[y - 1] == f and old_seed[y] == f and old_seed[y + 1] == e:
                seed[y] = e
            elif old_seed[y - 1] == f and old_seed[y] == f and old_seed[y + 1] == f:
                seed[y] = f
        print(''.join(seed)) #join all elements of list with no space between

tileprinter(seed, n)