import asyncio

from .client_1 import Client1
from .client_2 import Client2
from .client_3 import Client3


async def run_requests():
    client1 = Client1()
    client2 = Client2()
    client3 = Client3()
    print('running requests!')
    await asyncio.gather(
        client1.run_request(),
        client2.run_request(),
        client3.run_request()
    )
    print('requests finished!')
