buffer = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

n = input()
result = []
for i in buffer:
    n = n.replace(i, "*")

print(len(n))