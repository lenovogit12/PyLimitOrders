from trading_framework.execution_client import ExecutionClient
from trading_framework.price_listener import PriceListener





class LimitOrderAgent(PriceListener):

   def __init__(self, execution_client: ExecutionClient, product_id: str, limit_price: float, quantity: int, order_type: str) -> None:
        """

        :param execution_client: can be used to buy or sell - see ExecutionClient protocol definition
        """
        super().__init__()
        self.execution_client = execution_client
        self.product_id = product_id
        self.limit_price = limit_price
        self.quantity = quantity
        self.order_type = order_type

    def on_price_tick(self, product_id: str, price: float):
        if product_id == self.product_id:
            if self.order_type == 'buy' and price <= self.limit_price:
                self.execution_client.buy(self.product_id, self.quantity, self.limit_price)
                print(f"Placed a buy order for {self.quantity} units of {self.product_id} at {self.limit_price}")
            elif self.order_type == 'sell' and price >= self.limit_price:
                self.execution_client.sell(self.product_id, self.quantity, self.limit_price)
                print(f"Placed a sell order for {self.quantity} units of {self.product_id} at {self.limit_price}")


    
class MockExecutionClient(ExecutionClient):
    def buy(self, product_id: str, quantity: int, price: float):
        print(f"Buying {quantity} units of {product_id} at price {price}")

    def sell(self, product_id: str, quantity: int, price: float):
        print(f"Selling {quantity} units of {product_id} at price {price}")

execution_client = MockExecutionClient()
limit_order_agent = LimitOrderAgent(execution_client, product_id="IBM", limit_price=100.0, quantity=10, order_type='buy')
price_ticks = [("IBM", 95.5), ("IBM", 105.2), ("IBM", 98.3)]
for product_id, price in price_ticks:
    limit_order_agent.on_price_tick(product_id, price)




