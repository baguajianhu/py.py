import time
dog = {"藏獒":200,"牧羊犬":150,"中华田园犬":120,"哈士奇":100,"泰迪":50}   #狗血
monkey = {'公猴':300,"母猴":240,"老猴":160,"小猴":100,"幼猴":100}    #猴血
harm = {"藏獒":100,"牧羊犬":80,"中华田园犬":60,"哈士奇":40,"泰迪":20}   #狗的攻击
harm2 = {'公猴':70,"母猴":50,"老猴":30,"小猴":10,"幼猴":10}  #猴的攻击 
while True:
    c = '双方即将开战！！！'
    print(c.center(50,"-"))
    name = input("请输入要出战的狗：")
    print(name,dog[name])
    name2 = input('请输入要出战的猴子：')
    print(name2,monkey[name2])
    while True:
        dog[name] -= harm2[name2]   #狗的血量-要出战狗子的攻击
        print(f'狗的血量{dog[name]}')   #输出狗剩余血量
        monkey[name2] -= harm[name]     #出战的猴子 - 出战狗的攻击力 
        print(f'猴的血量{monkey[name2]}')   #输出猴剩余的血量
        time.sleep(1)
        if monkey[name2] <= 0 >= dog[name]: #如果出战猴子的血量<=0,出战的狗的血量<=0
            del dog[name]   #删除掉死亡的狗
            del monkey[name2]   #删除死亡的猴
            print(f"{name}和{name2}已死亡！！！！") #输出双方都已死亡
            break
        elif monkey[name2] <= 0: #如果猴子的血量<=0
            del monkey[name2]   #删除掉死掉的猴
            print(f"{name2}已死亡！！！！") #判定死亡
            break
        elif dog[name] <= 0:    #如果狗的血量<=0
            del dog[name]   #删掉死亡的狗
            print(f"{name}已死亡！！！！")  #判定死亡
            break
    print(dog)
    print(monkey)
    # if dog <= 0:
    #     print("狗的阵营全部阵亡！！！！")
    # elif monkey <= 0:
    #     print('猴子的阵营全部阵亡！！！')