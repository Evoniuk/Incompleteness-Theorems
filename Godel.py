def godel(x):
    number = {'0':1,'f':3,'~':5,'v':7,'a':9,'(':11,')':13,'X':17,'Y':289}
    primes = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61]
    z = 1
    index = 0
    for character in x:
        z = z*primes[index]**number[character]
        index += 1
    return z
