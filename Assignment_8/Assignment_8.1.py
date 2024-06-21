# 1. the two lists convert it into the dictionary

# keys = ['Ten', 'Twenty', 'Thirty']
# values = [10, 20, 30]
# Expected output:

# {'Ten': 10, 'Twenty': 20, 'Thirty': 30}

keys = [i for i in input("Enter list 1: ").split(" ")]
vals = [i for i in input("Enter list 2: ").split(" ")]
d=zip(keys,vals)
print(dict(d))