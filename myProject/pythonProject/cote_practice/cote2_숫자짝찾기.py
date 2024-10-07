answer = ''
x = "22345"
y = "012234"

list_x = []
list_y = []
ans_list = []
for i in range(len(x)):
    list_x.append(x[i:i + 1])
print(list_x)

for i in range(len(y)):
    list_y.append(y[i:i + 1])
print(list_y)

if len(list_x) > len(list_y):
    for i in range(len(list_x)):
        for j in list_y:
            if j == list_x[i]:
                ans_list.append(j)
elif len(list_x) <= len(list_y):
    for i in range(len(list_y)):
        for j in list_x:
            if j == list_y[i]:
                ans_list.append(j)
print(ans_list)