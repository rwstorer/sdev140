def print_leaving(leaving: str) -> None:
    print(leaving)

def print_greeting(greeting: str) -> None:
    print(greeting)
    print_leaving('Good bye')

hello: str = 'hello world'

print_greeting(hello)
print('done')
