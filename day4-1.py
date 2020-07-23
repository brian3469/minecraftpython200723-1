# -*- coding: utf-8 -*-
"""
Created on Thu Jul 23 09:55:25 2020

@author: user
"""

from mcpi.minecraft import Minecraft
mc = Minecraft.create()
x,y,z = mc.player.getTilePos()
n = 1

for i in range(10):
    for j in range(n):
        
        mc.spawnEntity(x,y,z,60)
        
    n =n * 2
    mc.postToChat("你生成了"+str(n)+"隻蠹魚")