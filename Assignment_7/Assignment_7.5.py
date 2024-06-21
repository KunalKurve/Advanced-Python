# 5. Create a list and exchange the values as index and index as values.
# lst=[12, 1, 3, 7, 8, 5, 8]
# 0 1 2 3 4 5 6

lst = [int(i) for i in input("Enter a list: ").split(" ")]
lst_indx = [-1]*(max(lst)+ 1)
for indx, d in enumerate(lst):
    lst_indx[d] = indx
print(lst_indx)