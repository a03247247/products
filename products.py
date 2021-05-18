import os

def read_file(filename):
    products = []       
    with open(filename, 'r', encoding = 'utf-8') as f:
        for line in f:
            if '商品,價錢' in line:
                continue  #繼續(跳過本次迴圈)
            name, price = line.strip().split(',')
            products.append([name, price])
    print(products)
    return products    

def uese_input(products):
    while True:
        name = input('請輸入商品名稱(輸入"q"離開)')
        if name == 'q':  #quit離開    
            break
        price = input('請輸入商品價格')        
        p =[]
        p.append(name)
        p.append(price)    #也可以寫成
        products.append(p) #products.append([name,price])
    print(products)
    return products

def print_products(products):
    for p in products:
        print(p[0],'的價格是',p[1])
       

def write_file(filename, products):
    with open(filename, 'w',encoding='utf-8') as f:
        f.write('商品,價錢\n')
        for p in products:
            f.write(p[0] + ',' + p[1] + '\n')


def main():
    filename= 'products.csv'
    if os.path.isfile(filename):
        print('讀取成功')
        products = read_file(filename)
    else:
         print('讀取失敗')

    products = uese_input(products)
    print_products(products)
    write_file('products.csv', products)

main()