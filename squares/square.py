import matplotlib.pyplot as plt
import numpy as np

def create(white=False, N=100):
    data = np.zeros((N, N))
    if(white):
        data = invert(data)
    return data

def paint(data, a, b, c, d, value=1, invert=False):
    data[a:b, c:d] = value
    if (invert):
        data = data.max() - data
    return data

def invert(data):
    if data.max() != 0:
        data = data.max() - data
    else:
        data = 1 - data
    return data


def display(data):
    plt.imshow(data, cmap='gray')
    plt.show()

def draw_line(data, x1, y1, x2, y2, value=1):
    length = max(abs(x2 - x1), abs(y2 - y1)) + 1

    xs = np.linspace(x1, x2, length).astype(int)
    ys = np.linspace(y1, y2, length).astype(int)

    data[xs, ys] = value
    return data

def all(n):
    data = create()
    match n:
        case 1:
            data = paint(data,40, 60, 40, 60)
        case 2:
            data = paint(data,40, 60, 40, 60)
            data = invert(data)
        case 3:
            data = paint(data, 40, 60, 30, 60)
        case 4:
            data = paint(data, 40, 60, 30, 60)
            data = invert(data)
        case 5:
            data = paint(data, 30, 60, 30, 31)
            data = invert(data)
        case 6:
            data = paint(data, 30, 60, 30, 31)
        case 7:
            data = paint(data, 40, 60, 30, 60, value=1)
            data = paint(data, 41, 59, 31, 59, value=0)
            data = paint(data, 50, 51, 31, 59, value=1)
        case 8:
            data = invert(data)
            data = paint(data, 40, 60, 30, 60, value=0)
            data = paint(data, 41, 59, 31, 59, value=1)
            data = paint(data, 50, 51, 31, 59, value=0)
        case 9:
            data = invert(data)
            data = paint(data, 40, 60, 30, 60, value=0)
            data = paint(data, 41, 59, 31, 59, value=1)
            data = paint(data, 41, 59, 45, 46, value=0)
            data = paint(data, 50, 51, 31, 59, value=0)
        case 10:
            data = paint(data, 40, 60, 30, 60, value=0)
            data = paint(data, 41, 59, 31, 59, value=1)
            data = paint(data, 41, 59, 45, 46, value=0)
            data = paint(data, 50, 51, 31, 59, value=0)
        case 11:
            data = paint(data, 10, 30, 10, 40, value=1)
            data = paint(data, 11, 29, 11, 39, value=0)
            data = draw_line(data, 10, 10, 29, 39)
            data = draw_line(data, 10, 39, 29, 10)
        case 12:
            data = paint(data, 10, 30, 10, 40, value=1)
            data = paint(data, 11, 29, 11, 39, value=0)
            data = draw_line(data, 10, 10, 29, 39)
            data = draw_line(data, 10, 39, 29, 10)
            data = invert(data)
        case 13:
            n = 8
            data = create(N=n)
            for i in range(n):
                for j in range(n):
                    data = paint(data, i, i+1, j, j+1, value=(i+j)%2)
        case 14:
            for i in range(100):
                data = paint(data, 0, 100, i, i+1, value=i)
        case 15:
            for i in range(100):
                data = paint(data, i, i+1, 0, 100, value=i)

        case 17:
            N = 1000
            data = create(N=1000)
            for i in range(N):
                value = (np.sin(2 * np.pi * i / 300) + 1) / 2
                data = paint(data, 0, N, i, i+1, value=value)

        case 19:
            N = 1000
            data = create(N=1000)
            for i in range(N):
                value = (np.exp( i / N)) 
                data = paint(data, 0, N, i, i+1, value=value)

        case 21:
            N = 100
            data = create(N=N)

            b = 50  
            c = 20   

            for i in range(N):
                value = np.exp(-((i - b)**2) / (2 * c**2))
                data = paint(data, 0, N, i, i+1, value=value)

        case 21:
            N = 100
            data = create(N=N)

            b = 50  
            c = 20   

            for i in range(N):
                value = np.exp(-((i - b)**2) / (2 * c**2))
                data = paint(data, 0, N, i, i+1, value=value)


        case 23:
            N = 100
            data = create(N=N)

            b = 50
            c = 10

            for i in range(N):
                value = np.exp(-abs(i - b) / c)
                data = paint(data, 0, N, i, i+1, value=value)

        case 27:
            N = 100
            data = create(N=100)
            mu = 0.5
            sigma = 0.15

            dist = np.random.normal(mu, sigma, N)
            for i in range(N):
                value = (np.sin(2 * np.pi * i / 30) + 1) / 2
                data = paint(data, 0, N, i, i+1, value=value)
            data = data + dist
        case 29:
            N = 100
            data = create(N=100)
            mu = 0.5
            sigma = 0.15

            d2 = np.random.normal(mu, sigma, N)
            d1= np.random.normal(mu, sigma, N)
            for i in range(N):
                v1 = (np.sin(2 * np.pi * i / 20) + 1) / 2
                v2 = (np.sin(2 * np.pi * i / 30) + 1) / 2
                value = v1 + v2
                data = paint(data, 0, N, i, i+1, value=value)
            dist = d1 + d2
            data = data + dist


        case 31:
            N = 100
            data = create(N=100)
            mu = 0.5
            sigma = 0.15
            b1 = 30
            b2 = 70
            c1 = 8 
            c2 = 12

            d2 = np.random.normal(mu, sigma, N)
            d1= np.random.normal(mu, sigma, N)
            for i in range(N):
                v1 = np.exp(-abs(i - b1) / c1)
                v2 = np.exp(-abs(i - b2) / c2)
                value = v1 + v2
                data = paint(data, 0, N, i, i+1, value=value)
            dist = d1 + d2
            data = data + dist

        case 33:
            N = 100
            data = create(N=N)

            b1 = 20
            b2 = 80
            c = 10
            mu = 0.5
            sigma = 0.15

            
            for i in range(N):
                v1 = np.exp(-((i - b1)**2) / (2 * c**2))
                v2 = np.exp(-abs(i - b2) / c)
                value = v1+v2
                data = paint(data, 0, N, i, i+1, value=value)
        case _:
            pass
            

    display(data)
    plt.show()
    plt.plot(data[50, :])
    plt.show()

all(17)
all(19)
all(21)
all(23)
all(27)
all(31)
all(33)
