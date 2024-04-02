from trading_framework.execution_client import ExecutionClient
from trading_framework.price_listener import PriceListener


class MockExecutionClient(ExecutionClient):
    def buy(self, product_id: str, quantity: int, price: float):
        print(f"Buying {quantity} units of {product_id} at price {price}")

    def sell(self, product_id: str, quantity: int, price: float):
        print(f"Selling {quantity} units of {product_id} at price {price}")



class LimitOrderAgent(PriceListener):

    def __init__(self, execution_client: ExecutionClient) -> None:
        """

        :param execution_client: can be used to buy or sell - see ExecutionClient protocol definition
        """
        super().__init__()

    def on_price_tick(self, product_id: str, price: float):
        # see PriceListener protocol and readme file
        pass
        if price > 100:
            self.execution_client.sell(product_id, 10, price)  # Example: Place a sell order if price is above 100
        else:
            self.execution_client.buy(product_id, 10, price)  # Example: Place a buy order if price is below or equal to 100

execution_client = MockExecutionClient()
limit_order_agent = LimitOrderAgent(execution_client)
price_ticks = [("BTCUSD", 95.5), ("BTCUSD", 105.2), ("BTCUSD", 98.3)]
for product_id, price in price_ticks:
    limit_order_agent.on_price_tick(product_id, price)


