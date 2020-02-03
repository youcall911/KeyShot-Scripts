# -*- coding: utf-8 -*-
# AUTHOR Luigi
# VERSION 0.0.1

# 快速生成一圈相机，用于制作360度转台GIF动画

# 用法：
# 先在Free Camera中调整好构图
# 然后渲染视窗空白处右键：居中并拟合模型
# 这一步推荐用快捷键：ctrl shift alt 鼠标右键
# 然后运行脚本

lux.newCamera("gif001")

# a 相机方位角，范围[-180, 180]
x = 10 #每个相机间隔的角度，经试验一般取10度，过渡均匀。值越小，图片越多，过渡越细腻
i = 24 #相机倾角，范围[-90, 90]，一般不用改，24度比较经典

# lux.getSphericalCamera("gif001")
#Get spherical information in degrees of active camera as a list: azimuth, inclination, and twist.

for a in range(-180,180,x):
    # print a
    name = "Gif_" + str(a)
    lux.newCamera(name)
    lux.setSphericalCamera(a,i)
    #Set spherical information of active camera: azimuth, inclination, and twist.
    #azimuth = The spherical azimuth in degrees [-180, 180]. *
    #incl = The spherical inclination in degrees [-90, 90]. *
    #twist = The spherical twist degrees [-180, 180]. *
    lux.saveCamera()
