import asyncio
import random


class Client:

    async def run_request(self):
        print(self.__class__.__name__)
        delay = random.randint(5, 10)
        print(f'sleeping {delay} seconds')
        await asyncio.sleep(delay)
        print(f'{self.__class__.__name__} request finished!')

