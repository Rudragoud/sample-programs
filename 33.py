names1 = ['Amir', 'Sridevi', 'Charlie']
names2 = [name.lower() for name in names1]
print(names2[2][0])


name1 = ['Amir', 'Sridevi','Charlie']
name2 = [name.lower() if name != 'Charlie' else 'chapline' for name in names1]
print(name2)
