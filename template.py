import imagelayer as il
import numpy as np
import cv2
from PIL import ImageFont, ImageDraw, Image

def template1(bgImg,fgImg,txt):
    h,w,channel = bgImg.shape
    if h/w<5/7:
        bgImg = bgImg[0:h,int(w/2-h*5.0/14.0):int(w/2+h*5.0/14.0)]#crop background
    else:
        bgImg = cv2.resize(bgImg,(571,800), interpolation=cv2.INTER_AREA) # crop background
    img = il.imgadd(fgImg, bgImg, [0.666,0.5], int(3*800/17), 800)
    h,w,channel = img.shape
    #put the txt img on the bg
    img_pil = Image.fromarray(img)
    draw = ImageDraw.Draw(img_pil)
    for i in range(len(txt)):
        if i == 0:
            # 绘制文字信息
            fontpath = "font/HanYiShangWeiShouShu/HYShangWeiShouShuW-1.ttf"
            font = ImageFont.truetype(fontpath, 60)
            tw,th=draw.textsize(txt[i], font=font)
            draw.text((int(0.5*w-0.5*tw),int(0.1*h-0.5*th)), txt[i], font=font, fill=(255, 0, 0))
            img = np.array(img_pil)
        else:
            fontpath = "font/HanYiShangWeiShouShu/HYShangWeiShouShuW-1.ttf"
            font = ImageFont.truetype(fontpath, 30)
            tw, th = draw.textsize(txt[i],font=font)
            draw.text((int(0.5*w-0.5*tw), int(0.8*h+th*(i-1)-0.5*th)), txt[i], font=font, fill=(255, 0, 0))
            img = np.array(img_pil)

    #少一个logo
    return img

def template2(bgImg,fgImg,txt):
    h, w, channel = bgImg.shape
    if h/w<5/7:
        bgImg = bgImg[0:h,int(w/2-h*5.0/14.0):int(w/2+h*5.0/14.0)]#crop background
    else:
        bgImg = cv2.resize(bgImg,(571,800), interpolation=cv2.INTER_AREA) # crop background
    img = il.imgadd(fgImg, bgImg, [0.833, 0.5], int(3 * 800 / 17), 800)
    h, w, channel = img.shape
    # put the txt img on the bg
    img_pil = Image.fromarray(img)
    draw = ImageDraw.Draw(img_pil)
    for i in range(len(txt)):
        if i == 0:
            # 绘制文字信息
 #           fontpath = "/Library/Fonts/Microsoft Sans Serif.ttf"
            fontpath = "font/庞门正道标题体/庞门正道标题体2.0增强版.ttf"
            font = ImageFont.truetype(fontpath, 80)
            tw, th = draw.textsize(txt[i], font=font)
            draw.text((int(0.5 * w - 0.5 * tw), int(0.2 * h - 0.5 * th)), txt[i], font=font, fill=(255, 255, 0))
            img = np.array(img_pil)
        else:
            fontpath = "font/庞门正道标题体/庞门正道标题体2.0增强版.ttf"
            font = ImageFont.truetype(fontpath, 35-5*i)
            tw, th = draw.textsize(txt[i], font=font)
            draw.text((int(0.5 * w - 0.5 * tw), int(0.35 * h + 2*th * (i - 1) - 0.5 * th)), txt[i], font=font,
                      fill=(255, 255, 0))
            img = np.array(img_pil)
    return img
def template3(bgImg,fgImg,txt):
    h, w, channel = bgImg.shape
    if h / w < 5 / 7:
        bgImg = bgImg[0:h, int(w / 2 - h * 5.0 / 14.0):int(w / 2 + h * 5.0 / 14.0)]  # crop background
    else:
        bgImg = cv2.resize(bgImg, (571, 800), interpolation=cv2.INTER_AREA)  # crop background
    fgImg = il.img_circle(fgImg)
    img = il.imgadd(fgImg, bgImg, [0.5, 0.5], int(1 * 800 / 2), 800)

    # put the txt img on the bg
    h, w, channel = img.shape
    img_pil = Image.fromarray(img)
    draw = ImageDraw.Draw(img_pil)
    for i in range(len(txt)):
        if i == 0:
            fontpath = "font/HanYiShangWeiShouShu/HYShangWeiShouShuW-1.ttf"
            font = ImageFont.truetype(fontpath, 80)
            tw, th = draw.textsize(txt[i], font=font)
            draw.text((int(0.5 * w - 0.5 * tw), int(0.2 * h - 0.5 * th)), txt[i], font=font, fill=(255, 255, 0))
            img = np.array(img_pil)
        else:
            fontpath = "font/HanYiShangWeiShouShu/HYShangWeiShouShuW-1.ttf"
            font = ImageFont.truetype(fontpath, 35 - 5 * i)
            tw, th = draw.textsize(txt[i], font=font)
            draw.text((int(0.5 * w - 0.5 * tw), int(0.35 * h + 2 * th * (i - 1) - 0.5 * th)), txt[i], font=font,
                      fill=(255, 255, 0))
            img = np.array(img_pil)
    return img

fgPath = 'foreground/WechatIMG62.png'
txt = [u"速度与激情",u"方向只有我一个 速度由我掌控",u"最高车速|燃油经济|操作稳定|行驶平顺"]

bgPath = 'background/WechatIMG63.jpeg'
fgImg = cv2.imread(fgPath, -1)
bgImg = cv2.imread(bgPath, -1)
img = template3(bgImg,fgImg,txt)
cv2.imwrite("results/results.png",img,[int(cv2.IMWRITE_PNG_COMPRESSION), 3])