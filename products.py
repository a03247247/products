import os

products = []

if os.path.isfile('products.csv'):
    print('讀取成功')
    #讀取檔案
    
    with open('products.csv', 'r', encoding = 'utf-8') as f:
        for line in f:
            if '商品,價錢' in line:
                continue  #繼續(跳過本次迴圈)
            name, price = line.strip().split(',')
            products.append([name, price])
    print(products)
else:
    print('讀取失敗')

while True:
    name = input('請輸入商品名稱')
    if name == 'q':  #quit離開    
        break
    price = input('請輸入商品價格')
    
    p =[]
    p.append(name)
    p.append(price)    #也可以寫成
    products.append(p) #products.append([name,price])
print(products)

for p in products:
    print(p[0],'的價格是',p[1])

with open('products.csv', 'w',encoding='utf-8') as f:
    f.write('商品,價錢\n')
    for p in products:
        f.write(p[0] + ',' + p[1] + '\n')