import math

def gcd(x, y):
    if x == 0:
        return y
    else:
        if y > x:
            return gcd(y - x, x)
        else:
            return gcd(x - y, y)

def main():
    inputs = input("Enter two numbers: ")
    inputs = inputs.split()
    print(gcd(int(inputs[0]), int(inputs[1])))

if __name__ == "__main__":
    main()
