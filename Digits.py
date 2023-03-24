k2, k3, k5, k6 = map(int, input().split())
temp1 = min(k2, k5, k6)
temp2 = min((k2 - temp1), k3)
ans = temp1 * 256 + temp2 * 32
print(ans)