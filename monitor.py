import asyncio
import logging
from datetime import datetime

logging.basicConfig(
    filename="network.log",
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

SERVICES = [
    ("Google DNS", "8.8.8.8", 53),
    ("Cloudflare HTTPS", "1.1.1.1", 443),
    ("Local SSH", "127.0.0.1", 22),
]

async def check_service(name, host, port):
    try:
        reader, writer = await asyncio.wait_for(
            asyncio.open_connection(host, port),
            timeout=3
        )
        writer.close()
        await writer.wait_closed()
        status = "UP"
    except (OSError, asyncio.TimeoutError) as error:
        status = f"DOWN ({type(error).__name__})"

    message = f"{name} | {host}:{port} | {status}"
    logging.info(message)
    print(f"{datetime.now():%Y-%m-%d %H:%M:%S} | {message}")

async def main():
    while True:
        await asyncio.gather(
            *(check_service(*service) for service in SERVICES)
        )
        await asyncio.sleep(60)

asyncio.run(main())
