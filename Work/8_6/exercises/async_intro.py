import asyncio

async def greeting(name):
    return f'Hello, {name}'

g = greeting('Guido')
print(g) # <coroutine object greeting at ...>
# sys:1: RuntimeWarning: coroutine 'greeting' was never awaited

async def main():
    names = ['Guido', 'Dave', 'Paula']
    for name in names:
        g = await greeting(name)
        print(g)


if __name__ == '__main__':
    asyncio.run(main())
    # Hello, Guido
    # Hello, Dave
    # Hello, Paula