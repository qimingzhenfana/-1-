print("输入数字：")
N = int(input())
count = 0
n = N
for i in range(32):
    if n & 1 == 1:
        count += 1
    n = n >> 1
print(N, "的二进制形式含有", count, "个 1")
