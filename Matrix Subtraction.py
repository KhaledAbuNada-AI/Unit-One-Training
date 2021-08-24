# Program to Subtraction two matrices using list comprehension

X = [[12,7,3],
    [4 ,5,6],
    [7 ,8,9]]

Y = [[5,8,1],
    [6,7,3],
    [4,5,9]]

result = [[X[i][j] - Y[i][j]  for j in range(len(X[0]))] for i in range(len(X))]

for r in result:
   print(r)

   ######### هنا نفس الحل ولكن بطريقة مختلفة وعدد سطور أكثر وهية أقل احترفية اما الطريقة الأول هية الاحترافية

# Program to Subtraction two matrices using nested loop

X = [[12,7,3],
    [4 ,5,6],
    [7 ,8,9]]

Y = [[5,8,1],
    [6,7,3],
    [4,5,9]]

result = [[0,0,0],
         [0,0,0],
         [0,0,0]]

# iterate through rows
for i in range(len(X)):
   # iterate through columns
   for j in range(len(X[0])):
       result[i][j] = X[i][j] - Y[i][j]

for r in result:
   print(r)
