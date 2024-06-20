
def f(n):
    f = 5*(n**2)
    return f

def g(n):
    g = n**2
    return g


if __name__ == "__main__":
    
    values = [1,10,100,1000]

    for n in values:
        delta = ((f(n)-g(n)) / f(n)) * 100
        print("n={:4d}, delta={}% ".format(n,round(delta,2)))


