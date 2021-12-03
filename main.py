# Hello World program in Python
    
print ("Hello World!");
print ("Hello", "Future", "Python", "Programmer!")
print ("Hello!", end="");\
print ("\nHello python is a great language")
print ("Hello", "Future", "Python", "Programmer!", sep="-")
print ("Hello", "Future", "Python", "Programmer!", sep="#")
print("Hello \"Python\" world")
print(1, 2, 3, 4, sep='#', end='&');
print("\nHello" + " " "future" + " " "python!\n")
print("Literals")
print(type(10))
print(type(45.50))
print("Operators\n")
print("Arithmetic Operator -**- Exponential\n")

print(2 ** 3)
print(2. ** 3.)
print(2 ** 3.)
print(2. ** 3)
print("\n")

print("Arithmetic Operator -*- Multiplication\n")
print(2 * 3)
print(2.* 3.)
print(2 * 3.)
print(2.* 3)
print("\n")

print("Arithmetic Operator -/- Division\n")
print(10 / 2)
print(10./ 2.)
print(10 / 2.)
print(10./ 2)
print("\n")

print("Arithmetic Operator -//- Floor Division\n")
print(10 // 2)
print(10.// 2.)
print(10 // 2.)
print(10.// 2)
print("\n")

print(6. / 4)
print(6.// 4)
print(6 / -4.)
print(6.// -4)
print("\n")


print("Arithmetic Operator -%- Modulo\n")
print(4 % 2)
print(5 % 2)
print("\n")

print("Arithmetic Operator -+- Addition\n")
print(6 + 4)
print(6.+ 4)
print(6.+ 4.)
print("\n")

print("Arithmetic Operator - Subtract\n")
print(6 - 4)
print(6.- 4)
print(6.- 4.)
print("\n")

print("Operator Hierarchy\n")
print(10 - 6 ** 2 / 9 *10 + 1)
print("\n")

print("Sub Expression\n")
print(2*(2+3))
print("\n")

print(2 * 3 ** 3 * 4)
print("\n")
print(13 / 4 + 13 % 4)
print("\n")
print(2 ** 3.)
print("\n")
print(10 - 6 ** 2 / 9 * 10 + 1)

print("\n")
x = 10 / 4
y = 5 / 2.0
print (x + y)
print("\n")

print(10 / 2)
print("\n")

print(2*(2+3))
print("\n")

print(6. // 4)



print("Arithmetic Operator -+- Addition\n")
print(6 + 4)
print(6.+ 4)
print(6.+ 4.)
print("\n")

print("Arithmetic Operator - Subtract\n")
print(6 - 4)
print(6.- 4)
print(6.- 4.)
print("\n")

print("Operator Hierarchy\n")
print(10 - 6 ** 2 / 9 *10 + 1)
print("\n")

print("Sub Expression\n")
print(2*(2+3))
print("\n")


print("\n")
amount_of_apple=2;
cost_of_apple=5;
COST_OF_APPLE=8;
print (amount_of_apple * cost_of_apple)
print("\n")
print (amount_of_apple * COST_OF_APPLE)
cost_of_apple = cost_of_apple + 5
print (amount_of_apple * cost_of_apple)

cost_of_apple += 5
print (amount_of_apple * cost_of_apple)

#Welcome to Python Programming

#x = 5
#y = 6
z = 7
print(x+y+z)

print(int(15.5)-10)
print ("ha" * -1)

#Num = input("Enter a Number: ") 
print ("Num" * 3 )



#Input Function & Type Cast
#age =input("My age is: ")
print ("age")

#inputString = input('Enter a string: ')
print("inputString"*2)

print(int(15.5)-10)

#Comparison Operators
x = 6
y = 7
print(x != y)
print("\n")

min_score = 13
score = 13

print(score > min_score)
print(score <= min_score)

print(2 < 4)

y = 20
#x = y += 3
print(x)

print('python'>'Python')

a = 5
b = 10
if b > a:
    print("b is greater than a")
    
x = 0
a = 6
b = 6
if a > 0:
    if b < 0: 
        x = x + 6 
    elif a > 6:
        x = x + 5
    else:
        x = x + 4
else:
    x = x + 3

print(x)


is_hungry = False
if(not is_hungry):
  print("You are not hungry")
else:
  print("You are hungry")
print("\n")

x = 6
y = 7
print(x == y)
print("\n")

is_hungry = True
if(not is_hungry):
  print("You are not hungry")
else:
  print("You are hungry")
print("\n")  

#BitWise Operators & ~ | ^

print(bin (15))
print("\n")
print(bin (22))
print("\n")
print(15 & 22)
print("\n")
print(15 | 22)
print("\n")
print(~22)
print("\n")
print(15 ^ 22)
#print(15 ~ 22)

print("\n")
print(22 >> 1)
print(22 >> 2)
print(22 >> 3)
print(22 >> 4)


print("\n")
print(22 << 1)
print(22 << 2)
print(22 << 3)
print(22 << 4)
print("\n")

print(int(1001))

print("\n")
a = 20
b = 5
print("a | b =", a | b)


print("\n")
list1 = [10, 11, 12, 13, 14]
print(list1[::3])

print("\n")
list1=[2,5,3,1]
print(list1[::-1])
print("\n")

#list1=[]+2

#list1=[] ++

list1 = [1, 2, 3, 4, 5]
list1[0] = 10
print(list1)



a = 5
b = 10
if b < a:
  print("a is greater than b")
elif a == b:
  b = 5
  print("a and b are equal")
else:
  print("b is greater than a")
  
  
x = 3
if ( x == 0 ):
  print("Am I here?")
elif ( x == 3 ):
  print("Or here?")
print("Or over here?")  

#List
list1 = [10, 20, 30, 40, 50]
list1.append(60)
print(list1)

print("\n")

list1=['h', 'e', 'l', 'l', 'o']
print(len(list1))


print("\n")
list1=['UK','India','Canada']
list1.insert(1,8)
print(list1)
print("\n")

ages = [56, 72, 24, 46]
ages.sort()
print(ages)
print("\n")

num = [4, 4, 3, 1]
num.sort()
print(num)
print("\n")

list1=["Go","Java","C","Rust"]
print(min(list1))
print("\n")

list1=["Go","Java","C","Python"]
print(max(list1))
print("\n")

list1 = [4, 4, 3, 1]
list1.pop(2)
print(list1)
print("\n")

for x in [0, 1, 1, 3]:
    for y in [0, 2, 1, 2]:
            print('*')

print("\n")

sum = 0
values = [2,9,1,7]
for number in values:
    sum += number

print(sum)

print("\n")

for x in [0, 2, 1, 3]:
    for y in [0, 4, 1, 2]:
            print('*')

print("\n")

for letter in 'KodeKloud':
    if letter == 'u':
        continue
    print('Letter : ' + letter)

print("\n")

for letter in 'KodeKloud':
    if letter == 'e':
        continue
    print('Letter : ' + letter)
print("\n")

sum = 0
values = [2,9,1,7]
for number in values:
    sum = sum + number

print(sum)
print("\n")

#List Contd

letters = ["A", "B", "C", "D", "E"]
print(letters[1:])
print("\n")
list1=[]*2
list1=[]
list1=["USA","Canada","India"]

print("\n")
list1 = [[1,2,3,2,5],[4,5,6,7],[8,9,10]]
for i in list1:
      if len(i)==3:
        print(i)
print("\n")
list1 = [10, 11, 12, 13, 14]
print(list1[0])

print("\n")
list1 = [1, 2, 3, 4]
for index, j in enumerate(list1):
     print(index, j)

print("\n")
list1 = [10, 11, 12, 13, 14]
list1.append(15)
print(list1)


print("\n")
list1 = [10, 11, 12, 13, 14]
print(list1[::1])


print("\n")
list1 = [[1,2,3,2,5],[4,5,6,7],[8,9,10]]
for i in list1:
      if len(i)==4:
        print(i)

print("\n")
list1=[4,0,7,1]
print(list1[::-1])


print("\n")
list1 = [1, 2, 3, 4]
for i, j in enumerate(list1):
     print(i, j)


print("\n")

my_list = [0, 1, 2, 3, 4]
print(my_list[-1])


print("\n")
my_list = [0, 1, 2, 3, 4]
my_list.append("python")
print(my_list[2:])

print("\n")

my_list = [0, 1, 2, 3, 4]
print(my_list[::3])

print("\n")
my_list = [0, 1, 2, 3, 4]
print(my_list[::-1])

print("\n")
my_list = [0, 1, 2, 3, 4]
my_list.append("python")
b = my_list[1:]
print(b)
print("\n")
my_list = [0, 1, 2, 3, 4]
print(my_list[::2])


print("\n")
list1 = [1, 66, "python", [11, 55, "cat"], [ ], 2.22, True]
print(list1[2:4])


list1=[3,4,6,1,2]
list2=list1
list1[0]=9
print(list2)


print("\n")
my_list = [0, 3, 4, 1, 2]
print(my_list.index(1))

print("\n")
list1=[3,4,6,1,2]
list2=list1
list1[1]=9
print(list2)

print("\n")
countries = ["USA", "Canada", "India"]
countries[0], countries[1] = countries[1], countries[0]
print(countries)


print("\n")
list1 = [0, 3, 4, 1, 2]
list1[2:5]=[8,9]
print(list1)


print("\n")
Li = ['A','C','b', 1, 3, 4]
print(Li)


print("\n")
my_list = [0, 1, 2, 3, 4]
print(my_list.index(2))


print("\n")
list1 = [0, 3, 4, 1, 2]
list1[1]=[8,9]
print(list1)



print("\n")
list1 = [0, 3, 4, 1, 2]
list1[2:4]=[1,2]
print(list1)



print("\n")
(4, 6) not in [(4, 7), (5, 6), "hello"]



print("\n")
a = []
for i in range(5):
    a.append([])
    for j in range(5):
        a[i].append(j)
print(a[2][3])


print("\n")
countries = [['Egypt', 'USA', 'India'],
       ['Dubai', 'America', 'Spain'], 
       ['London', 'England', 'France']]
countries2  = [country for sublist in countries for country in 
                       sublist if len(country) < 6]
print(countries2)

print("\n")
a = []
for i in range(2):
    a.append([])
    for j in range(2):
        a[i].append(j)

print(a)


print("\n")
matrix = [[0, 1, 2], [0, 1, 2], [0, 1, 2]]

matrix2 = []

for submatrix in matrix:
  for val in submatrix:
    matrix2.append(val)

print(matrix2[2])


print("\n")
matrix = [[j for j in range(3)] for i in range(3)] 
print(matrix[2][1])
print("\n")

a = []
for i in range(5):
    a.append([])
    for j in range(5):
        a[i].append(j)

print(a[3][3])

print("\n")
matrix = [[0, 1, 2], [0, 1, 2], [0, 1, 2]]

matrix2 = []

for submatrix in matrix:
  for val in submatrix:
    matrix2.append(val)

print(matrix2[0])

countries = [['Egypt', 'USA', 'India'], ['Dubai', 'America', 'Spain'], ['London', 'England', 'France']]
countries2  = [country for sublist in countries for country in sublist if len(country) < 4]
print(countries2)

matrix = [[j for j in range(3)] for i in range(3)] 
print(matrix[1][2])

matrix = [[j for j in range(4)] for i in range(4)] 
print(matrix[3][1])

#Nested List 3D
matrix = [[[k for k in range(3)] for j in range(3)] for i in range(3)]
print(matrix[2][1])

matrix = [[[k for k in range(3)] for j in range(3)] for i in range(3)]
print(matrix[1][2])

matrix = [[[k for k in range(3)] for j in range(3)] for i in range(3)]
print(matrix[0][0][1])

matrix = [[[0, 1, 2], [0, 1, 2], [0, 1, 2]], [[0, 1, 2], [0, 1, 2], [0, 1, 2]], [[0, 1, 2], [0, 1, 2], [0, 1, 2]]]

matrix2 = []

for submatrix in matrix:
  for val in submatrix:
    matrix2.append(val)

print(matrix2[2][0])


matrix = [[[0, 1, 2], [0, 1, 2], [0, 1, 2]], [[0, 1, 2], [0, 1, 2], [0, 1, 2]], [[0, 1, 2], [0, 1, 2], [0, 1, 2]]]

matrix2 = []

for submatrix in matrix:
  for val in submatrix:
    matrix2.append(val)

print(matrix2[2][2])


matrix = [[[0, 1, 2], [0, 1, 2], [0, 1, 2]], [[0, 1, 2], [0, 1, 2], [0, 1, 2]], [[0, 1, 2], [0, 1, 2], [0, 1, 2]]]

matrix2 = []

for submatrix in matrix:
  for val in submatrix:
    matrix2.append(val)

print(matrix2[2])


print("\n")
list1 = [1, 66, "python", [11, 55, "cat"], [ ], 2.22, True]
print(list1[0:4])

print("\n")
my_list = [0, 1, 2, 3, 4]
print(my_list[2:4])
print("\n")


print("\n")



print("\n")

list1 = [1, 66, "python", [11, 55, "cat"], [ ], 2.22, True]
print(list1.upper())

