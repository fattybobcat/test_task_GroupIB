import asyncio
import sys


async def check_port(ip, port, loop):
    conn = asyncio.open_connection(ip, port, loop=loop)
    try:
        reader, writer = await asyncio.wait_for(conn, timeout=0.1)
        print(ip, port, "OPEN")
        if port in (443, 80):
            pass
        return (ip, port, "OPEN")
    except Exception as e:
        return e
    finally:
        if "writer" in locals():
            writer.close()


def port_treatment(ports):
    return [int(p[:-1]) if "," in p else int(p) for p in ports]


async def check_port_sem(sem, host, port, loop):
    async with sem:
        return await check_port(host, port, loop)


async def run(host, diapason, ports, loop):
    sem = asyncio.Semaphore(400)  # Change this value for limitation
    tasks = []
    host_mask = ".".join(host.split(".")[:-1])
    for d in range(diapason[0], diapason[1] + 1):
        for p in ports:
            host = f"{host_mask}.{d}"
            tasks.append(asyncio.ensure_future(
                check_port_sem(sem, host, p, loop)))
    responses = await asyncio.gather(*tasks)
    return responses


if __name__ == "__main__":

    if len(sys.argv) < 3:
        print("""Program requires two parameters:
              """)
        sys.exit(-1)
    hosts, *band = sys.argv[1].split("/")
    diapason = (int(hosts.split(".")[-1]),
                int(band[0]) if band else int(hosts.split(".")[-1]))
    ports = port_treatment(sys.argv[2:])
    loop = asyncio.get_event_loop()
    future = asyncio.ensure_future(run(hosts, diapason, ports, loop))
    loop.run_until_complete(future)
