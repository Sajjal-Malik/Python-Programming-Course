d = {"tom":53525342345, "bob":123235235123, "jacob":3152334234}

print(d)

print(d["tom"])

print(d.keys())

print(d.items())

print(d.values())

d["sam"] = 44546464632

print(d)

del d["jacob"]

print(d)

for key in d:
    print("key is:", key, "and it's value is:", d[key])


print("tom" in d)
print("sam" in d)
print("joe" in d)

print(d.clear())

print(d)




tup = (5, 9)

print(tup[1])

# tup[1] = 23     # this shows that tuples are immutable

print(tup)

