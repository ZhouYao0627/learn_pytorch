from torch.utils.tensorboard import SummaryWriter
from torchvision import transforms
from PIL import Image

# python的用法 ---> tensor数据类型
# 通过transforms.ToTensor去看两个问题
# 1.transforms该如何使用(python)
# 2.为什么我们需要Tensor数据类型

img_path = 'dataset/train/ants_image/0013035.jpg'
img = Image.open(img_path)

writer = SummaryWriter("logs")

# 1.transforms该如何使用(python)
tensor_trans = transforms.ToTensor()
tensor_img = tensor_trans(img)

writer.add_image("Tensor_img", tensor_img)

writer.close()
