#把99乘法表包裝成函式, 可做n1xn2乘法
def list(n1=10,n2=10):
    for n1 in range(1,10):
        for n2 in range(1,10):
            print(n1,"*",n2,"=",n1*n2)


#四則運算包裝成函式
def count(n1,n2,op):  
    if op=="+":
        print(n1+n2)
    elif op=="-":
        print(n1-n2)
    elif op=="*":
        print(n1*n2)
    elif op=="/":
        print(n1/n2)
    else :
        print("運算錯誤")