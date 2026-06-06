from PIL import Image
import matplotlib.pyplot as plt
import numpy as np

TARGET_WIDTH = 500

path = 'spectrum_py/'

def vis_compare(s, t):
    x = np.arange(0, len(s))
    plt.plot(x, s)
    plt.plot(x, t)
    plt.show()

def get_spec(name):
    img = Image.open(f"{path}/{name}.png")
    img = img.resize((TARGET_WIDTH, img.height))
    img_array = np.array(img)
    s = img_array[:, :, 0]
    s = s.mean(axis=0)
    s = 255 - s
    return s

templates = {'A': [], 'B': [], 'F': [], 'G': [], 'K': [], 'M': [], 'O': []}

t = get_spec('test')
for i in templates.keys():
    templates[i] = get_spec(i)

min = None 
ind = None
for k in templates:
    res = (templates[k] - t)**2
    mean = res.mean()
    if (min == None or min > mean):
        min = mean
        ind = k

print(f"Closest matchness: {ind}, {min}")
if (ind != None):
    vis_compare(templates[ind], t)

