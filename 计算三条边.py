a = float(input("Please enter three edges:"))
b = float(input("Please enter three edges:"))
c = float(input("Please enter three edges:"))
# 这是它们的三条边
if a + b > c and a + c > b and b + c > a:
    print("可以构成一个三角形")
    # n = float(input("周长为："))
    n = a + b + c
    print(f"周长为：{n}")
    p = n / 2
    m = (p * (p - a) * (p - b) * (p - c)) ** 0.5
    print("面积%.2f" % m)

else:
    print("不可以构成一个三角形")