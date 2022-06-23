year = int(input("请您输入年份："))
if year % 4 == 0 and year %100 != 0 or year % 400 == 0:
    print(f"{year},这是一个闰年")
else:
    print(f"{year},这是一个平年")
