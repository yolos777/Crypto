# coding=utf-8
import json
import websockets
import time
import asyncio

async def main():
    url = "wss://stream.binance.com:9443/stream?streams=xrpusdt@miniTicker/adausdt@miniTicker"
    async with websockets.connect(url) as client:
        print(client)
        while True:
            market_price = json.loads(await client.recv())['data']
            real_time = time.localtime(market_price['E'] // 1000) # для перевода времени из миллисекунд в нормальное для понимание
            print(market_price['c'], "at", f"{real_time.tm_hour}:{real_time.tm_min}:{real_time.tm_sec}")

if __name__ == '__main__':
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(main())

