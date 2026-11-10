# 상품 클래스
class Product () :
    number = 1
    def __init__(self, name, price, stock):
        self.number = Product.number
        self.name = name
        self.price = price
        self.stock = stock
        product_list.append(self)
        Product.number += 1

# 장바구니
class Cart():
    def __init__(self):
        self.cart_list = []
    def add(self, product_num, qty):
        for item in cart.cart_list : 
            if item['product_num'] == product_num : 
                item['cart_qty'] += qty
                return 
         
        self.cart_list.append({
            "product_num":product_num,
            "cart_qty" : qty
        })
        
        
    def minus(self, product_num) : 
        self.cart_list.remove(product_num)
        print(self.cart_list)
    def view_cart(self) :
        pro_price = 0
        total_price = 0
        if not self.cart_list:
            print("장바구니가 비어있습니다.")
        for cart_item in self.cart_list:
            for product_item in product_list:
                if product_item.number == cart_item['product_num'] : 
                    pro_price = (product_item.price) * (cart_item['cart_qty'])
                    total_price += pro_price
                    print(f"{product_item.name}     x{cart_item['cart_qty']}   {pro_price}원")
        print("-" * 40)
        print(f"상품 합계 : {total_price :>10}원")
        if total_price <= 20_000 :
            total_price += 3000
            print("배송비 : \t3000원")
# 쿠폰
class Coupon(): 
    def __init__(self):
        pass

product_list = []  

product1 = Product('마우스', 89_000, 10)
product2 = Product('마우스패드', 9_000, 0)
product3 = Product('노트북', 1_199_000, 5)
product4 = Product('모니터', 119_000, 13)
product5 = Product('가습기', 49_000, 7)

# 상품 조회 함수
def view_product(product_list) : 
    print("번호 \t 상품명 \t 가격 \t\t 재고")
    for item in product_list : 
        print(f"{item.number} \t {item.name} \t {item.price}원 \t {item.stock if item.stock != 0 else '0 (품절)'}")

# 장바구니 담기
def cart_insert() :
    product_num = int(input("상품번호 : "))
    product_qty = int(input("수량 :"))

    for item in product_list : 
        if item.number == product_num :
            if item.stock >= product_qty :
                item.stock -= product_qty
                cart.add(product_num, product_qty)
                print(f"{item.name} {product_qty}개를 담았습니다.")
            else :
                print(f"재고가 부족합니다. (담을 수 있는 수량 : {item.stock})")
        

def cart_remove():
    product_num = int(input("상품번호 : "))

    for item in cart.cart_list : 
        if item['product_num'] == product_num :
            cart.minus(item)
        
    print(f"장바구니에서 제거했습니다. ")


user_input = 0
cart = Cart()
while True :
    print('-' * 40)
    print("1. 상품목록 2. 담기 3. 빼기 4. 장바구니 5. 쿠폰 6. 결제 q. 종료")
    print('-' * 40)
    user_input = input("선택 : ")

    if user_input == '' : 
        continue

    elif user_input.lower() == 'q' :
        break

    
    if user_input == "1" : 
        view_product(product_list)
    elif user_input == "2" :
        cart_insert()
    elif user_input == "3" : 
        cart_remove()
    elif user_input == "4" : 
        cart.view_cart()



