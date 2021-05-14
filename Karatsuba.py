

def karatsuba(num1, num2, result=0):
    # Assuming len(num) is a power of 2 (e.g. 2, 4, 8, 16, ...) and len(num1) == len(num2)
    num1s, num2s = str(num1), str(num2)
    if len(num1s) == len(num2s) and (len(num1s) % 2 == 0 and len(num2s) % 2 == 0 or len(num1s) == 1):
        n = len(num1s)
        if n > 1:
            a, b, c, d = int(num1s[:int(n/2)]), int(num1s[int(n/2):]), int(num2s[:int(n/2)]), int(num2s[int(n/2):])
            ac = result + karatsuba(a, c, result)
            bd = result + karatsuba(b, d, result)
            rest = (a+b)*(c+d) - ac - bd
            return int(ac*pow(10, n) + rest*pow(10, n/2) + bd)
        else:
            return num1*num2

    else:
        print("Please make sure both numbers have equal digits and are powers of 2")


if __name__ == '__main__':
    print(karatsuba(1455, 5645))
