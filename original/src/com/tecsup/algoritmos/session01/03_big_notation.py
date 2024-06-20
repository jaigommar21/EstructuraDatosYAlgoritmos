
def f(n):
    f = n**4 + 100*n**2 + 10*n +50
    return f

def g(n):
    g = n**4
    return g


if __name__ == "__main__":
    
    values = [1,10,100,1000]

    for n in values:
        delta = ((f(n)-g(n)) / f(n)) * 100
        print("n={:4d}, delta={}% ".format(n,round(delta,2)))


