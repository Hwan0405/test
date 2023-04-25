# data = []
# with open('test.txt', 'r') as h:
#     for t in h:
#         data.append(t.strip())
# print(data)

a = []
count = 0
with open ('reviews.txt', 'r') as f:
    for b in f:
        a.append(b.strip())
        count += 1
        if count % 1000 == 0:
            print(len(a))
print(len(a))

sum_len = 0
for c in a:
    sum_len += len(c)
    print(sum_len)
print('平均長度為：', sum_len/len(a))

new = []
for d in a:
    if len(d) < 100:
        new.append(d)
print('total comment length less than 100:', len(new))
print(new[1])