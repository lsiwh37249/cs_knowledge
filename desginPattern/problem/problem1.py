class Order:
    def __init__(self, order_type):
        self.order_type = order_type

    def process_order(self):
        if self.order_type == "online":
            return "Processing online order"
        elif self.order_type == "store":
            return "Processing store order"
        else:
            return "Unknown order type"

# 클라이언트 코드
order1 = Order("online")
print(order1.process_order())

order2 = Order("store")
print(order2.process_order())

order3 = Order("unknown")
print(order3.process_order())

# 이 코드의 문제점
# 'Order' 클래스가 모든 주문 유형을 처리하고 있어 단일 책임 원칙을 위반
# 새로운 주문 유형을 추가할 때마다 'process_order' 메서드 수정


