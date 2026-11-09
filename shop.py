# 상품 클래스
class Product () :
    id = 1
    def __init__(self, name, price, stock):
        self.id = Product.id
        self.name = name
        self.price = price
        if stock == 0 :
            self.stock = "0 (품절)"
        else : self.stock = stock
        # product_list.append(self)
        Product.id += 1

# 장바구니
class Cart():
    def __init__(self):
        self.cart_list = []
    def add(self, item): 
        self.cart_list.append(item)
    def minus(self, item) : 
        self.cart_list.remove(item)
    def view_cart(self, item) :
        print(item)

# 쿠폰
class Coupon(): 
    def __init__(self):
        pass



product1 = Product('마우스', 89000, 10)
product2 = Product('마우스패드', 9000, 0)
product3 = Product('노트북', 1199000, 5)
product4 = Product('모니터', 119000, 13)
product5 = Product('가습기', 49000, 7)

product_list = [
    product1,
    product2,
    product3,
    product4,
    product5

]

def menu() :
    user_input = 0

    while True :
        print('-' * 40)
        print("1. 상품목록 2. 담기 3. 빼기 4. 장바구니 5. 쿠폰 6. 결제 q. 종료")
        print('-' * 40)
        user_input = input("선택 : ")

        if user_input == '' : 
            continue
        elif int(user_input) > 0 and int(user_input) < 7 :
            break
        elif user_input.lower() == 'q' :
            break

    return user_input

# 상품 조회 함수
def view_product(product_list) : 
    print("번호 \t 상품명 \t 가격 \t\t 재고")
    for item in product_list : 
        print(f"{item.id} \t {item.name} \t {item.price}원 \t {item.stock}")

# 장바구니 담기
def cart_insert() :

    product_num = int(input("상품번호 : "))
    if product_list[product_num].stock == 0 :
        print("품절된 상품입니다.")
        return
    
    product_qty = int(input("수량 :"))

    print("11111",product_qty)
    print("22222",product_list[product_num].stock)

    if product_qty <= product_list[product_num].stock :
        product_list[product_num].stock -= product_qty
        print(product_list[product_num].stock)
        print(f"{product_list[product_num].name} {product_qty}개를 담았습니다.")
        cart = Cart()
        cart.add(product_list[product_num], product_qty)
    else :
        print(f"재고가 부족합니다. (담을 수 있는 수량 : {product_list[product_num].stock})")
        
        





print(product_list)

user_input = menu()
if user_input == "1" : 
    view_product(product_list)
elif user_input == "2" :
    
    cart_insert()


