from cryptofeed import FeedHandler
from cryptofeed.exchanges import Binance
from cryptofeed.defines import TRADES
import time
import asyncio


async def handle_trade(trade, receipt_timestamp):
    print("TRADE:")
    print("symbol:", trade.symbol)
    print("side:", trade.side)
    print("price:", trade.price)
    print("amount:", trade.amount)
    print("timestamp:", trade.timestamp)
    print("receipt:", receipt_timestamp)

def main():
    print("hola")
    fh = FeedHandler()
    fh.add_feed(
        Binance(
            symbols=['BTC-USDT'],
            channels=[TRADES],
            callbacks={TRADES:handle_trade})

    )
    fh.run()

if __name__ == "__main__":
    main()