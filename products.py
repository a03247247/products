products = []
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

with open('products.csv', 'w') as f:
    for a in products:
        f.write(p[0] + ',' + p[1] + '\n')