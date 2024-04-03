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
super().__init__()
        self.execution_client = execution_client
        self.product_id = product_id
        self.limit_price = limit_price
        self.quantity = quantity
        self.order_type = order_type

    def on_price_tick(self, product_id: str, price: float):
        class MockExecutionClient(ExecutionClient):
    def buy(self, product_id: str, quantity: int, price: float):
        print(f"Buying {quantity} units of {product_id} at price {price}")

    def sell(self, product_id: str, quantity: int, price: float):
        print(f"Selling {quantity} units of {product_id} at price {price}")

execution_client = MockExecutionClient()



