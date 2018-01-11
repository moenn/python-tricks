'''
difference between shallow copy and deepcopy.
Reproduced from https://stackoverflow.com/a/17246744/6815755
2018/1/12
'''
import copy


a = [1, 2, 3]
b = [4, 5, 6]
c = [a, b]

d = copy.copy(c)
e = copy.deepcopy(c)

print("{}\n{}\n{}".format(id(c), id(d), id(e)))
print("\n")
print("{}\n{}\n{}".format(id(c[0]), id(d[0]), id(e[0])))