import random
import numpy as np
import imagelayer as il
import numpy as np
import cv2
from PIL import ImageFont, ImageDraw, Image
from random import choice

def template1(bgImg ,fgImg) :
    h, w, channel = bgImg.shape
    if h/w < 7/5:
        bgImg = bgImg[0:h, int(w/2-h*5.0/14.0):int(w/2+h*5.0/14.0)]#crop background
    else:
        bgImg = cv2.resize(bgImg,(571,800), interpolation=cv2.INTER_AREA) # crop background

    img = il.imgadd(fgImg, bgImg, [0.666,0.5], int(3*800/17), 800)

    return img, [[0.5, 0.1], [0.5, 0.8]]


def template2(bgImg, fgImg):
    h, w, channel = bgImg.shape
    if h/w < 7/5:
        bgImg = bgImg[0:h,int(w/2-h*5.0/14.0):int(w/2+h*5.0/14.0)]#crop background
    else:
        bgImg = cv2.resize(bgImg,(571,800), interpolation=cv2.INTER_AREA) # crop background

    img = il.imgadd(fgImg, bgImg, [0.866, 0.5], int(3 * 800 / 17), 800)

    return img, [[0.5, 0.2], [0.5, 0.35]]

def template3(bgImg, fgImg):
    h, w, channel = bgImg.shape
    if h / w < 7 / 5:
        bgImg = bgImg[0:h, int(w / 2 - h * 5.0 / 14.0):int(w / 2 + h * 5.0 / 14.0)]  # crop background
    else:
        bgImg = cv2.resize(bgImg, (571, 800), interpolation=cv2.INTER_AREA)  # crop background
    fgImg = il.img_circle(fgImg)

    img = il.imgadd(fgImg, bgImg, [0.5, 0.5], int(1 * 800 / 2), 800)

    return img, [[0.5, 0.2], [0.5, 0.35]]

def template4(bgImg,fgImg,logoImg):
    h, w, channel = bgImg.shape
    if h/w<7/5:
        bgImg = bgImg[0:h,int(w/2-h*5.0/14.0):int(w/2+h*5.0/14.0)]#crop background
    else:
        bgImg = cv2.resize(bgImg,(571,800), interpolation=cv2.INTER_AREA) # crop background
    img = il.imgadd(fgImg, bgImg, [0.65, 0.5], int(0.5 * 800), 800)

    img = il.imgadd(logoImg, img, [0.1, 0.8], int(3 * 800 / 17), 800)

    # img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    # img = Image.fromarray(img)
    # img = stylize(img, './style_transfer/saved_models/cyberpunk.pth')
    # img = np.array(img)
    # img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
    #logo
    return img, [[0.5, 0.2], [0.5, 0.35]]

def choosetemplate(bgPath,fgPath):
    logoImg = cv2.imread('logo/leksas.png',-1)#读取logo的文件路径
    fgImg = cv2.imread(fgPath, -1)
    bgImg = cv2.imread(bgPath, -1)
    # fg_img_color = il.img_color()
    # print(fg_img_color)
    h,w,channel=fgImg.shape
    if h < w :
        img, txtpos = random.choice([template1, template2,template3])(bgImg,fgImg)
    else:
        img, txtpos = template4(bgImg, fgImg, logoImg)
    cv2.imwrite("results/results_notext.png",img,[int(cv2.IMWRITE_PNG_COMPRESSION), 3])
    return "results/results_notext.png", txtpos

def addtxt(ImgPath,txt,txtpos):
    img = cv2.imread(ImgPath,-1)
    h, w, channel = img.shape
    #txt_color
    image = Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    color = il.img_color(image)
    print(color)
    # put the txt img on the bg
    img_pil = Image.fromarray(img)
    draw = ImageDraw.Draw(img_pil)
    fontpath = ["font/庞门正道标题体/庞门正道标题体2.0增强版.ttf",
                "font/HanYiShangWeiShouShu/HYShangWeiShouShuW-1.ttf",
                "font/ZhanKuKuaiLeTi/ZhanKuKuaiLeTi2016XiuDingBan-1.ttf",
                "font/zhengqingke/zhengqingkehuangyou.ttf",
                "font/siyuan/SourceHanSansSC-Bold.otf"]
    foo = choice(fontpath)
    for i in range(len(txt)):
        if i == 0:
            # 绘制文字信息
            font = ImageFont.truetype(foo, 80)
            tw, th = draw.textsize(txt[i], font=font)
            draw.text((int(txtpos[0][0] * w - 0.5 * tw), int(txtpos[0][1] * h - 0.5 * th)), txt[i], font=font, fill=(255-color[2], 255-color[1], 255-color[0]))
            img = np.array(img_pil)
        else:
            font = ImageFont.truetype(foo, 35 - 5 * i)
            tw, th = draw.textsize(txt[i], font=font)
            draw.text((int(txtpos[1][0] * w - 0.5 * tw), int(txtpos[1][1] * h + 2 * th * (i - 1) - 0.5 * th)), txt[i], font=font,
                      fill=(255-color[2], 255-color[1], 255-color[0]))
            img = np.array(img_pil)
    cv2.imwrite("results/results.png", img, [int(cv2.IMWRITE_PNG_COMPRESSION), 3])

if __name__=="__main__":
    fgPath = 'foreground/WechatIMG62.png'
    txt = [u"速度与激情",u"方向只有我一个 速度由我掌控",u"最高车速|燃油经济|操作稳定|行驶平顺"]
    bgPath = 'background/WechatIMG59.jpeg'
    image = Image.open(bgPath)
    print(il.img_color(image))
    imgPath, txtPos = choosetemplate(bgPath,fgPath)
    addtxt(imgPath,txt,txtPos)