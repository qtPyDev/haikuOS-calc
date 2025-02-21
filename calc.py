# this is a basic python calc in haikuOS
# written by qtPyDev



class Operators:
    def __init__(self):
        self.add = '+' 
        self.sub = '-'
        self.div = '/'
        self.mul = '*'


def add(a, b) -> int:
    return a+b


def sub(a, b) -> int:
    return a-b


def div(a, b) -> int:
    return a/b


def mul(a,b) -> int:
    return a*b


def main():
    oprs = Operators()
    num1 = int(input('\nnum1: '))
    opr = str(input('\noperator: '))
    num2 = int(input('\nnum2: '))

    ans = 0
    match opr:
        case oprs.add:
            ans = add(num1, num2)
        case oprs.sub:
            ans = sub(num1, num2)
        case oprs.div:
            ans = div(num1, num2)
        case oprs.mul:
            ans = mul(num1, num2)
        case _:
            print('\nincorrect operator !')
            main()

    print(f'\n{ans}')


if __name__=='__main__':
	main()
