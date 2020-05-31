import random
def up_bulu(seq):
    for i in range(len(seq)-1):
        for j in range(len(seq)-1-i):
            if seq[j]>seq[j+1]:
                seq[j+1],seq[j]=seq[j],seq[j+1]
    return seq

b=[12,3,54,56,33,6,235,66,43]

print(b)
print(up_bulu(b))