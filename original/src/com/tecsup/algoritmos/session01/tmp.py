#list_numbers=[1, 10, 100, 1000, 10000, 100000]

from timeit import default_timer as timer

n=10 #0000

start=timer()
for i in range(0,n):
    print(f"i = {i}")
end=timer()
delay=end-start
print(f"> Time {delay}")


n=1 #0000

for i in range(0,n):
    print(f"i={i}")


n=1 #0000

for i in range(0,n):
    print(f"i={i}")



n=10 #0000

for i in range(0,n):
    for j in range(0,n):
        print(f"i = {i} and j = {j} ")

n = 10
# Execute n times 
for i in range(0,n):
    print(f"i={i}")
# Outer loop executed n times
for i in range(0,n):
    for j in range(0,n):
        print(f"i = {i} and j = {j} ")

n = 10
if n == 1:
    print("Wrong value")
    print("n=",n)
else:
    for i in range(0,n):
        print(f"i={i}")