from torch.utils.tensorboard import SummaryWriter
from PIL import Image
import numpy as np

writer = SummaryWriter("logs")
img_path = "data/train/bees_image/95238259_98470c5b10.jpg"
img_PIL = Image.open(img_path)
img_array = np.array(img_PIL)

writer.add_image("train", img_array, 1, dataformats='HWC')
# y = x
for i in range(100):
    writer.add_scalar("y=2x", 2 * i, i)

writer.close()
