import array as arr
a = arr.array('i',[1,2,3])
# for i in a :
#   print(a.index(i), ' = ', i)

  ## adding elements in array
a.insert(2,1)
for i in a :
  print(i)

a.append(5)
print('this is appeand',a[4])


## accessing elements from the array

print(a[4])

a.remove(5)
for i in a:
  print('i', i )
a.pop(0)
def prnt(arr):
  for i in arr:
    print('\tthis is print function\t',i)


prnt(a)