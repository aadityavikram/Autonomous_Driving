import numpy as np
from PIL import Image

file = np.load('D:/PycharmProjects/Self_Driving/Autonomous_Driving/data/training_data-1.npy')
img = Image.fromarray(file[0], 'RGB')
img.show()
