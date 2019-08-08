import random
import numpy as np
import imagelayer as il
import numpy as np
import cv2
from PIL import ImageFont, ImageDraw, Image
from random import choice

def template1(bgImg ,fgImg,logoImg) :
    h, w, channel = bgImg.shape
    if h/w < 7/5:
        bgImg = bgImg[0:h, int(w/2-h*5.0/14.0):int(w/2+h*5.0/14.0)]#crop background
    else:
        bgImg = cv2.resize(bgImg,(571,800), interpolation=cv2.INTER_AREA) # crop background

    img = il.imgadd(fgImg, bgImg, [0.666,0.5], int(3*800/17), 800)

    return img, [[0.5, 0.15], [0.5, 0.8], [0, 0]]#[fx,fy],[left(-1)/center(0)/right(1),horizontal(0)/vertical(1)]


def template2(bgImg, fgImg, logoImg):
    h, w, channel = bgImg.shape
    if h/w < 7/5:
        bgImg = bgImg[0:h,int(w/2-h*5.0/14.0):int(w/2+h*5.0/14.0)]#crop background
    else:
        bgImg = cv2.resize(bgImg,(571,800), interpolation=cv2.INTER_AREA) # crop background

    img = il.imgadd(fgImg, bgImg, [0.866, 0.5], int(3 * 800 / 17), 800)

    return img, [[0.5, 0.2], [0.5, 0.35], [0, 0]]

#文字的方向和放置有问题
def template3(bgImg, fgImg, logoImg):
    h, w, channel = bgImg.shape
    if h / w < 7 / 5:
        bgImg = bgImg[0:h, int(w / 2 - h * 5.0 / 14.0):int(w / 2 + h * 5.0 / 14.0)]  # crop background
    else:
        bgImg = cv2.resize(bgImg, (571, 800), interpolation=cv2.INTER_AREA)  # crop background
    fgImg = il.img_circle(fgImg)

    img = il.imgadd(fgImg, bgImg, [0.5, 0.5], int(1 * 800 / 2), 800)

    return img, [[0.75, 0], [0.9, 0], [-1, 1]]

def template4(bgImg,fgImg,logoImg):
    h, w, channel = bgImg.shape
    if h/w<7/5:
        bgImg = bgImg[0:h,int(w/2-h*5.0/14.0):int(w/2+h*5.0/14.0)]#crop background
    else:
        bgImg = cv2.resize(bgImg,(571,800), interpolation=cv2.INTER_AREA) # crop background
    img = il.imgadd(fgImg, bgImg, [0.65, 0.5], int(0.6154 * 800), 800)

    img = il.imgadd(logoImg, img, [0.03846, 0.889], int(1 * 800 / 13), 800)

    return img, [[0.5, 0.1346], [0.5, 0.25], [0, 0]]

def template5(bgImg,fgImg,logoImg):
    h, w, channel = bgImg.shape
    if h/w < 7/5:
        bgImg = bgImg[0:h,int(w/2-h*5.0/14.0):int(w/2+h*5.0/14.0)]#crop background
    else:
        bgImg = cv2.resize(bgImg,(571,800), interpolation=cv2.INTER_AREA) # crop background
    img = il.imgadd(fgImg, bgImg, [0.6, 0.3], int(19/36* 800), 800)
    img_final = il.imgadd(logoImg, img, [0.1, 0.1], int(0.1 * 800), 800)
    return img_final,[[0.95, 0.1], [0.95, 0.35], [1, 0]]

def template6(bgImg,fgImg,logoImg):
    h, w, channel = bgImg.shape
    if h/w<7/5:
        bgImg = bgImg[0:h,int(w/2-h*5.0/14.0):int(w/2+h*5.0/14.0)]#crop background
    else:
        bgImg = cv2.resize(bgImg,(571,800), interpolation=cv2.INTER_AREA) # crop background
    img = il.imgadd(fgImg, bgImg, [0.45, 0.5], int(3/17*800), 800)
    img_final = il.imgadd(logoImg, img, [0.95, 0.9], int(0.1 * 800), 800)
    return img_final, [[0.1, 0.1],[0.1, 0.7], [-1, 0]]

def choosetemplate(bgPath,fgPath):
    logoImg = cv2.imread('logo/leksas.png',-1)#读取logo的文件路径
    fgImg = cv2.imread(fgPath, -1)
    bgImg = cv2.imread(bgPath, -1)
    # fg_img_color = il.img_color()
    # print(fg_img_color)
    h,w,channel=fgImg.shape
    if h < w :
        img, txtpos = random.choice([template1, template2, template3, template6])(bgImg,fgImg,logoImg)
        #img, txtpos = template3(bgImg,fgImg,logoImg)
    else:
        img, txtpos = random.choice([template4, template5])(bgImg,fgImg,logoImg)
    cv2.imwrite("results/results_notext.png",img,[int(cv2.IMWRITE_PNG_COMPRESSION), 3])
    return "results/results_notext.png", txtpos

def addtxt(ImgPath,txt,txtpos):
    img = cv2.imread(ImgPath,-1)
    h, w, channel = img.shape
    #choose txt_color by image background
    image = Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    bg_color = il.img_color(image)
    print(bg_color)
    txt_color = il.complement(bg_color[0],bg_color[1],bg_color[2])
    print(txt_color)
    #chooose txt place direction
    switcher = {
        -1 : [0,0], #左上角
        0 : [-0.5,-0.5], #中间
        1 : [-1,0]  #右上角
    }
    k = switcher.get(txtpos[-1][0],[-0.5,-0.5])
    print(k)
    # put the txt img on the bg
    draw = ImageDraw.Draw(image)
    fontpath = ["font/庞门正道标题体/庞门正道标题体2.0增强版.ttf",
                "font/HanYiShangWeiShouShu/HYShangWeiShouShuW-1.ttf",
                "font/ZhanKuKuaiLeTi/ZhanKuKuaiLeTi2016XiuDingBan-1.ttf",
                "font/zhengqingke/zhengqingkehuangyou.ttf",
                "font/siyuan/SourceHanSansSC-Bold.otf"]
    foo = choice(fontpath)

    if txtpos[-1][1] == 0:
        for i in range(len(txt)):
            if i == 0:
                # 绘制文字信息
                font = ImageFont.truetype(foo, 80, encoding='utf-8')
                tw, th = draw.textsize(txt[i], font=font)
                draw.text((int(txtpos[0][0] * w + k[0] * tw), int(txtpos[0][1] * h + k[1] * th)), txt[i], font=font,
                              fill=(txt_color[0], txt_color[1], txt_color[2]))
            else:
                font = ImageFont.truetype(foo, 35 - 5 * i, encoding='utf-8')
                tw, th = draw.textsize(txt[i], font=font)
                draw.text((int(txtpos[1][0] * w + k[0] * tw), int(txtpos[1][1] * h + 4 * th * (i - 1) + k[1] * th)), txt[i],
                              font=font,fill=(txt_color[0], txt_color[1], txt_color[2]))
    else:
        for i in range(len(txt)):
            if i == 0:
                right = 0  # 往右位移量
                down = 0  # 往下位移量
                row_hight = 0  # 行高设置（文字行距）
                word_dir = 0;  # 文字间距
                font = ImageFont.truetype(foo, 80, encoding='utf-8')
                tw, th = draw.textsize(txt[i], font=font)
                for j, s2 in enumerate(txt[i]):
                    draw.text((int(txtpos[0][0] * w + k[0] * tw + right),
                               int(txtpos[0][1] * h + k[1] * th + down)), s2, font=font,
                              fill=(txt_color[0], txt_color[1], txt_color[2]))  # 设置位置坐标 文字 颜色 字体
                    if j == 0:
                        ww, wh = font.getsize(s2)
                    if s2 == "," or s2 == "\n":  # 换行识别
                        right = right + ww + row_hight
                        down = 0
                        continue
                    else:
                        down = down + wh + word_dir
            else:
                right = 0  # 往右位移量
                down = 0  # 往下位移量
                row_hight = 0  # 行高设置（文字行距）
                word_dir = 0;  # 文字间距
                font = ImageFont.truetype(foo, 35 - 5 * i, encoding='utf-8')
                tw, th = draw.textsize(txt[i], font=font)
                for j, s2 in enumerate(txt[i]):
                    draw.text((int(txtpos[1][0] * w + k[0] * tw) + right,
                               int(txtpos[1][1] * h + k[1] * th) + down), s2, font=font,
                              fill=(txt_color[0], txt_color[1], txt_color[2]))  # 设置位置坐标 文字 颜色 字体
                    if j == 0:
                        ww, wh = font.getsize(s2)
                    if s2 == "," or s2 == "\n":  # 换行识别
                        right = right + ww + row_hight
                        down = 0
                        continue
                    else:
                        down = down + wh + word_dir
    img = np.array(image)
    img = cv2.cvtColor(img,cv2.COLOR_RGB2BGR)
    cv2.imwrite("results/results.png", img, [int(cv2.IMWRITE_PNG_COMPRESSION), 3])

if __name__=="__main__":
    fgPath = 'foreground/WechatIMG62.png'
    txt = [u"速度与激情", u"方向只有我一个\n速度由我掌控"]
    #txt = [u"速度与激情",u"方向只有我一个\n 速度由我掌控",u"最高车速|燃油经济|操作稳定|行驶平顺"]
    bgPath = 'background/WechatIMG58.jpeg'
    imgPath, txtPos = choosetemplate(bgPath,fgPath)
    addtxt(imgPath,txt,txtPos)
    il.complement_image('results/results.png','results/results_complementary.png')