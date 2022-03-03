
print("---------LINEAR CONGRUENTIAL----------")

#X0 is the seed
#a is the multiplier constant
#c is an additive constant
#m is the modulus
#x0>0, a>0, c>0, m>0 must be intergers.


def linearCongrential(x0, a, c, m):

    mod = m - 1
    array = []
    array.append(x0)
    xa = 0
    while xa not in array:
        x1 = (a * x0 + c) % m
        x0 = x1
        array.append(x1)
        print(array)
        r1 = x1 / mod
        print(r1)
        xa = (a * x0 + c) % m


linearCongrential(37, 19, 33, 100)

print("---------MULTIPLICATIVE LINEAR CONGRUENTIAL----------")

#m = 2^g
#a = 3 + 8k, or a = 5 + 8k
#k must be an integer
#g must be an interger
#x0 must be an odd integer
#under these conditions the period is maximum: N = m/4 = 2^g-2

def multiplicativeLinear(x0, k, g):
    m = pow(2, g)
    mod = m - 1
    array = []
    array.append(x0)
    xa = 0
    while xa not in array:
        a = (5 + 8 * k)
        x1 = (a * x0) % m
        x0 = x1
        array.append(x1)
        print(array)
        r1 = x1/mod
        print(r1)
        xa = (a * x0) % m

multiplicativeLinear(17, 2, 5)

print("--------ADDITIVE CONGRUENTIAL GENERATOR-------")

def additiveCongrential(x1, x2, x3, m):
    mod = m - 1
    arrayseed = [x1, x2, x3]
    xa = 0
    n = 2
    i = 0
    while xa not in arrayseed:

        seed = arrayseed[i]
        xi = seed
        seed = arrayseed[i + n]
        xi = (seed + xi) % m
        print(xi)
        arrayseed.append(xi)    #[65, 89, 98, 63]
        r1 = xi / mod
        print(r1)
        i = i + 1
        seed = arrayseed[i]
        xa = (seed + xi) % m
        print(arrayseed)


additiveCongrential(65, 89, 98, 100)