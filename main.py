import numpy as np

def calculate(x,y):
    return (x**x)+np.abs(y)

def main():
    x = 8
    y = -9.4
    z = calculate(x,y)
    print(z)

if __name__ == '__main__':
    main()