import os
import numpy as np
import torch
from torchvision import datasets, transforms
from PIL import Image

def crop106(img):
    return transforms.functional.crop(img, 0, 0, 106, 106)

class lakhDSTrain(torch.utils.data.Dataset):
    def __init__(self):
        self.main_dir = '/home/hice1/hkumawat3/scratch/midi2img/res2val/'
        self.transform = transforms.Compose([
                                #transforms.Lambda(crop106),
                                transforms.Pad(padding=(0,75,0,75)),
                                transforms.ToTensor()])
        self.total_imgs = os.listdir(self.main_dir)
        self.keys = None


    def __len__(self):
        return len(self.total_imgs)

    def __getitem__(self, idx):
        img_loc = os.path.join(self.main_dir, self.total_imgs[idx])

        tensor_image = torch.zeros((256,3,256))
        #tensor_image = torch.zeros((106,3,106))

        try:
                image = Image.open(img_loc).convert("RGB")
                tensor_image = self.transform(image)
        except OSError:
               print("Image error") 

        example = dict()
        example["image"] = np.array(tensor_image).astype(np.float32).transpose(1,2,0)
        return example


class lakhDSValid(torch.utils.data.Dataset):
    def __init__(self):
        self.main_dir = '/home/hice1/hkumawat3/scratch/midi2img/res2small/'
        #self.transform = transforms.Compose([transforms.Pad(padding=(0,75,0,75)),
        self.transform = transforms.Compose([
                                #transforms.Lambda(crop106),
                                transforms.Pad(padding=(0,75,0,75)),
                                transforms.ToTensor()])
        self.total_imgs = os.listdir(self.main_dir)
        self.keys = None


    def __len__(self):
        return len(self.total_imgs)

    def __getitem__(self, idx):
        img_loc = os.path.join(self.main_dir, self.total_imgs[idx])
        tensor_image = torch.zeros((256,3,256))
        #tensor_image = torch.zeros((106,3,106))

        try:
                image = Image.open(img_loc).convert("RGB")
                tensor_image = self.transform(image)
        except OSError:
                print("Image error") 

        example = dict()
        example["image"] = np.array(tensor_image).astype(np.float32).transpose(1,2,0)
        return example


