#!/usr/bin/env python3
#-*-cofing:utf-8-*-
# OpenAI-gym DQN tutorial
# カートの上に棒が立てられており、棒が倒れきらないようにカートを動かして棒のバランスを整えるゲームです。
# １ステップごとに棒が倒れなければ、+1 の報酬が与えられ、棒が倒れた時点でゲームが終了し、-1 の得点が与えられます。
# つまり、棒を倒さないようにカートを左右に動かしながら、どれだけ長く保てるかを競うゲームです。
import gym
import math
import random
import copy #---
import numpy as np
import pandas as pd
import time
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns #---
from collections import namedtuple, deque #---
from itertools import count #---
from PIL import Image #---

import torch
import torch.nn as nn #---
import torch.optim as optim #---
import torch.nn.functional as F #---
import torchvision.transforms as T #---

import settings

# ゲーム環境を作る（カートポールのウィンドウを立ち上げます）
env = gym.make('CartPole-v0').unwrapped

def get_sreen(env, resize):

