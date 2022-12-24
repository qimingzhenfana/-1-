print("输入数字：")
n = int(input())
count = 0
for i in range(32):
    if n & (1 << i) == (1 << i):
        count += 1
print(n, "的二进制形式含有", count, "个 1")
