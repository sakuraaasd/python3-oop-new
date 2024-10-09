
a = [1,2,3]
b = [1,'abc',2.0,['a','b','c']]
print(a)
print(b)

print('a[0]=',a[0])

print(b[1:3])
c = b[1:3]
print(c,type(c))

s = 'abcde'
print(s[1:3],s[-1])

a = {
  "a" : 1,
  'c' : 2,
  'd' : 3
}
print(a)

s = {1,2,3,4}
s.add(5)
print(s)

l = [1,2,3,4,5]
l.append(6)
print(l)

a = '1234512'
s1 = set(a)
print(s1)

s1 = {1,2,3,4}
s2 = {3,4,5,6}

print(s1 & s2)
print(s1 | s2)
