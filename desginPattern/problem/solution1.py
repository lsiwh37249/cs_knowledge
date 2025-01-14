from abc import ABC, abstractmethod

# 추상 제품 클래스
class Order(ABC):
    @abstractmethod
    def process(self):
        pass

# 구체적인 제품 클래스들
class OnlineOrder(Order):
    def process(self):
        return "Processing online order"

class StoreOrder(Order):
    def process(self):
        return "Processing store order"

class UnknownOrder(Order):
    def process(self):
        return "Unknown order type"

# 팩토리 클래스
class OrderFactory:
    @staticmethod
    def create_order(order_type):
        if order_type == "online":
            return OnlineOrder()
        elif order_type == "store":
            return StoreOrder()
        else:
            return UnknownOrder()

# 클라이언트 코드
order1 = OrderFactory.create_order("online")
print(order1.process())

order2 = OrderFactory.create_order("store")
print(order2.process())

order3 = OrderFactory.create_order("unknown")
print(order3.process())
