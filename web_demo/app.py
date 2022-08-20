from flask import Flask, render_template, request
import os
import numpy as np
import torch
import torch.nn as nn
import torch.nn.functional as F
from hilbert_curve import hilbertize_arr
import cv2
import random
import sys

class CNN(nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = nn.Conv2d(1, 4, 3, padding=1)
        self.pool = nn.MaxPool2d(2, 2)
        self.conv2 = nn.Conv2d(4, 8, 2, padding=1)
        self.conv3 = nn.Conv2d(8, 16, 1, padding=0)
        self.batch_norm1 = nn.BatchNorm2d(4)
        self.batch_norm2 = nn.BatchNorm2d(4)
        self.batch_norm3 = nn.BatchNorm2d(4)
        self.dropout = nn.Dropout(p=0.2)
        self.dropout2 = nn.Dropout(p=0.2)
        self.l1 = nn.Linear(1024, 256)
        self.l2 = nn.Linear(256, 128)
        self.l3 = nn.Linear(128, 64)
        self.out = nn.Linear(64, 1)

    def forward(self, x):
        x = F.relu(self.conv1(x))
        x = self.pool(x)
        x = self.dropout(x)
        
        x = F.relu(self.conv2(x))
        x = self.pool(x)
        x = self.dropout(x)
        
        x = F.relu(self.conv3(x))
        x = self.pool(x)
        x = self.dropout(x)

        x = torch.flatten(x)

        x = F.relu(self.l1(x))
        x = self.dropout2(x)

        x = F.relu(self.l2(x))
        x = self.dropout2(x)
        
        x = F.relu(self.l3(x))
        x = self.dropout2(x)

        x = torch.sigmoid(self.out(x))

        return x

def cutoff_idx(arr: list, buffer) -> int:
    arr = list(arr)
    arr.reverse()

    for i in range(len(arr)):
        if sum(arr) >= buffer:
            # if count > buffer:
            return len(arr) - 1 - i

def crop_img(img: np.ndarray, buffer: int) -> np.ndarray:
    # h_idx = cutoff_idx(img[0, :], buffer)
    # v_idx = cutoff_idx(img[:, 0], buffer)

    arrs = []
    for i in range(15):
        idx = random.randint(0, len(img[0]) // 2)
        if random.randint(0, 1) == 1:
            arrs.append(img[idx, :])
        else:
            arrs.append(img[:, idx])

    print(arrs)

    idxs = []
    for arr in arrs:
        cutoff = cutoff_idx(arr, buffer)
        if cutoff != None:
            idxs.append(cutoff)

    b_idx = max(idxs)

    return img[:b_idx, :b_idx]

def pad_img(img: np.ndarray, des_w: int) -> np.ndarray:
    while len(img[:, 0]) < des_w:
        row = np.zeros((1, len(img[0, :]), 3))
        img = np.vstack((img, row))
    while len(img[0, :]) < des_w:
        col = np.zeros((len(img[:, 0]), 1, 3))
        img = np.column_stack((img, col))

    return img

def rescale_img_arrs(arr):
    narr = []
    for i in range(len(arr)):
        if arr[i].shape[0] < 64:
            narr.append(pad_img(arr[i], 64))
        else:
            print(arr[i].shape)
            img = cv2.resize(arr[i].astype(np.uint8), (64, 64))
            narr.append(img)

    return narr

app = Flask(__name__)

@app.route('/upload')
def up():
    return render_template('upload.html')

@app.route('/uploader', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']

        f_ext = f.filename[-5:].split('.')[1]
        f.save(f'./up_files/upload.{f_ext}')

        file_name = os.listdir('./up_files')[0]
        bytes = [f"{n:08b}" for n in open('./up_files/' + file_name, "rb").read()]
        for i in range(len(bytes)):
            bytes[i] = int(bytes[i], 2)

        # bytes = bytes.astype(np.uint8)

        arr = hilbertize_arr(bytes)
        # print(np.array(arr))
        arr = crop_img(np.array(arr), 5)
        arr = rescale_img_arrs([arr])[0]
        # arr = arr.astype(np.uint8)

        msaved = torch.load('./models/model_87')
        nmodel = CNN()
        nmodel.load_state_dict(msaved) 
        pred = nmodel(torch.Tensor([arr]))
        # print(arr)
        # .detach.cpu.numpy()[0]

        if pred[0] < 0.5:
            diagnosis = 'not malicious'
            pred = 1.0 - pred
        else:
            diagnosis = 'malicious'

        return f'File is {diagnosis} | {round(float(pred[0]*100), 4)}% Certainty'

if __name__ == '__main__':
    app.run(debug=True)