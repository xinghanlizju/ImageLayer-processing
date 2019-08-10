import random
import imagelayer as il
import cv2
from PIL import ImageFont, ImageDraw, Image
from random import choice
from math import ceil

def template1(bgPath ,fgPath,txt) :
    bgImg = cv2.imread(bgPath, -1)
    fgImg = cv2.imread(fgPath, -1)
    h, w, channel = bgImg.shape
    if h / w < 7 / 5:
        bgImg = bgImg[0:h, int(w / 2 - h * 5.0 / 14.0):int(w / 2 + h * 5.0 / 14.0)]  # crop background
        bgImg = cv2.resize(bgImg, (774, 1080), interpolation=cv2.INTER_AREA)  # crop background
    else:
        bgImg = cv2.resize(bgImg, (774, 1080), interpolation=cv2.INTER_AREA)  # crop background
    #生成后的背景大小
    hi, wi, channeli = bgImg.shape
    #前景大小
    hf, wf, channelf = fgImg.shape

    #选择合适的前景大小
    fg_hsize=min(0.666*wi*hf/wf,0.666*hi)

    img = il.imgadd(fgImg, bgImg, [0.66, 0.5], round(fg_hsize), 1080)#前景、背景、前景位置、前景大小、背景大小

    #生成文字的图像
    ROI_txt = img[int(hi / 6):int(5*hi/6), int(wi / 6):int(5*wi/6)]
    txtImage(txt, "horizontal", ROI_txt)
    pos = [[0.5, 0.15, 0], [0.5, 0.8, 0], [0.952, 0.95, 0]]

    print("template 1")
    return img, pos

def template2(bgPath ,fgPath,txt):
    bgImg = cv2.imread(bgPath, -1)
    fgImg = cv2.imread(fgPath, -1)
    h, w, channel = bgImg.shape
    if h / w < 7 / 5:
        bgImg = bgImg[0:h, int(w / 2 - h * 5.0 / 14.0):int(w / 2 + h * 5.0 / 14.0)]  # crop background
        bgImg = cv2.resize(bgImg, (774, 1080), interpolation=cv2.INTER_AREA)  # crop background
    else:
        bgImg = cv2.resize(bgImg, (774, 1080), interpolation=cv2.INTER_AREA)  # crop background

    hi, wi, channeli = bgImg.shape
    # 前景大小
    hf, wf, channelf = fgImg.shape

    # 选择合适的前景大小
    fg_hsize = min(0.666 * wi * hf / wf, 0.666 * hi)

    img = il.imgadd(fgImg, bgImg, [0.866, 0.5], round(fg_hsize), 1080)


    #生成文字的图像和位置
    ROI_txt = img[int(hi / 7):int(6 * hi / 7), int(wi / 6):int(5 * wi / 6)]
    txtImage(txt,"horizontal",ROI_txt)
    pos = [[0.5, 0.2, 0], [0.5, 0.4, 0], [0.05, 0.95, 0]]

    print("template 2")
    return img, pos

def template3(bgPath ,fgPath,txt):
    bgImg = cv2.imread(bgPath, -1)
    fgImg = cv2.imread(fgPath, -1)
    h, w, channel = bgImg.shape

    if h / w < 7 / 5:
        bgImg = bgImg[0:h, int(w / 2 - h * 5.0 / 14.0):int(w / 2 + h * 5.0 / 14.0)]  # crop background
        bgImg = cv2.resize(bgImg, (774, 1080), interpolation=cv2.INTER_AREA)  # crop background
    else:
        bgImg = cv2.resize(bgImg, (774, 1080), interpolation=cv2.INTER_AREA)  # crop background

    fgImg = il.img_circle(fgImg)

    img = il.imgadd(fgImg, bgImg, [0.5, 0.5], int(1 * 1080 / 2), 1080)

    hi, wi, channeli = img.shape
    ROI_txt = img[int(1*hi / 9):int(8 * hi / 9), int(wi / 6):int(5 * wi / 6)]

    txtImage(txt,"vertical", ROI_txt)
    pos = [[0.99, 1/9, 1], [0.1, 0.5, 0], [0.5, 0.95, 0]]

    print("template 3")
    return img, pos

def template4(bgPath ,fgPath,txt):
    bgImg = cv2.imread(bgPath, -1)
    fgImg = cv2.imread(fgPath, -1)
    h, w, channel = bgImg.shape
    if h / w < 7 / 5:
        bgImg = bgImg[0:h, int(w / 2 - h * 5.0 / 14.0):int(w / 2 + h * 5.0 / 14.0)]  # crop background
        bgImg = cv2.resize(bgImg, (774, 1080), interpolation=cv2.INTER_AREA)  # crop background
    else:
        bgImg = cv2.resize(bgImg, (774, 1080), interpolation=cv2.INTER_AREA)  # crop background

    hi, wi, channeli = bgImg.shape
    # 前景大小
    hf, wf, channelf = fgImg.shape

    # 选择合适的前景大小
    fg_hsize = min(0.666 * wi * hf / wf, 0.666 * hi)
    img = il.imgadd(fgImg, bgImg, [0.65, 0.5], round(fg_hsize), 1080)

    ROI_txt = img[0:hi, int(wi / 6):int(5 * wi / 6)]
    txtImage(txt, "horizontal", ROI_txt)

    txtpos = [[0.5, 0.1346, 0], [0.5, 0.3, 0], [0.95, 0.95, 0]]

    print("template 4")
    return img, txtpos

def template5(bgPath ,fgPath,txt):
    bgImg = cv2.imread(bgPath, -1)
    fgImg = cv2.imread(fgPath, -1)
    h, w, channel = bgImg.shape
    if h / w < 7 / 5:
        bgImg = bgImg[0:h, int(w / 2 - h * 5.0 / 14.0):int(w / 2 + h * 5.0 / 14.0)]  # crop background
        bgImg = cv2.resize(bgImg, (774, 1080), interpolation=cv2.INTER_AREA)  # crop background
    else:
        bgImg = cv2.resize(bgImg, (774, 1080), interpolation=cv2.INTER_AREA)  # crop background
    hi, wi, channeli = bgImg.shape
    hf, wf, channelf = fgImg.shape
    fg_hsize = min(0.7 * wi * hf / wf, 0.7 * hi)
    img = il.imgadd(fgImg, bgImg, [0.6, 0.3], round(fg_hsize), 1080)

    ROI_txt = img[int(hi / 2):hi, int(wi / 2):wi]
    txtImage(txt, "horizontal", ROI_txt)
    txtpos = [[0.9, 0.1, 1], [1, 0.6, 1], [0.1, 0.1, 0]]
    print("template 5")
    return img, txtpos

def template6(bgPath ,fgPath,txt):
    bgImg = cv2.imread(bgPath, -1)
    fgImg = cv2.imread(fgPath, -1)
    h, w, channel = bgImg.shape
    if h/w<7/5:
        bgImg = bgImg[0:h,int(w/2-h*5.0/14.0):int(w/2+h*5.0/14.0)]#crop background
        bgImg = cv2.resize(bgImg, (774, 1080), interpolation=cv2.INTER_AREA)  # crop background

    else:
        bgImg = cv2.resize(bgImg,(774,1080), interpolation=cv2.INTER_AREA) # crop background

    hf, wf, channelf = fgImg.shape

    # 选择合适的前景大小
    fg_hsize = min(0.8 * w * hf / wf, 0.8 * h)
    img = il.imgadd(fgImg, bgImg, [0.5, 0.5], int(fg_hsize), 1080)
    ROI_txt = img[0:int(h / 2), 0:int(w / 2)]
    txtImage(txt, "horizontal", ROI_txt)
    txtpos = [[0.05, 0.05, -1], [0.05, 0.8, -1], [0.952, 0.95, 0]]
    print("template 6")
    return img, txtpos

def choosetemplate(bgPath,fgPath,txt):
    fgImg = cv2.imread(fgPath, -1)
    h, w, channel = fgImg.shape
    if 5*h < 7*w :
        img, txtpos = random.choice([template1, template2, template3, template6])(bgPath,fgPath,txt)
    else:
        img, txtpos = random.choice([template4, template5])(bgPath,fgPath,txt)
    cv2.imwrite("results/results_notext.png",img,[int(cv2.IMWRITE_PNG_COMPRESSION), 3])
    return "results/results_notext.png", txtpos

def txtImage(txt,direction,img):
    if direction =="horizontal":
        h, w, channel = img.shape
        # choose txt_color by image background
        image = Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
        bg_color = il.img_color(image)
        txt_color = [255 - bg_color[0], 255 - bg_color[1], 255 - bg_color[2]]

        # put the txt img on the bg
        draw = ImageDraw.Draw(image)
        fontpath = ["font/庞门正道标题体/庞门正道标题体2.0增强版.ttf",
                    "font/HanYiShangWeiShouShu/HYShangWeiShouShuW-1.ttf",
                    "font/ZhanKuKuaiLeTi/ZhanKuKuaiLeTi2016XiuDingBan-1.ttf",
                    "font/zhengqingke/zhengqingkehuangyou.ttf",
                    "font/siyuan/SourceHanSansSC-Bold.otf"]
        foo = choice(fontpath)

        # create the txt image
        for i in range(len(txt)):
            if i == 0:
                # 绘制文字信息
                font = ImageFont.truetype(foo, 80, encoding='utf-8')
                tw, th = draw.textsize(txt[i], font=font)
                # 换行处理
                if tw > w:
                    txt_str = txt[i].splitlines()
                    for k in range(len(txt_str)):
                        strw, strh = draw.textsize(txt_str[k], font=font)
                        if strw > w:
                            count = ceil(tw / w)
                            for j in range(count-1):
                                txt_str[k] = txt_str[k][:(j+1)*ceil((len(txt_str[k])-j)/count)+j] + '\n' + \
                                         txt_str[k][(j+1)*ceil((len(txt_str[k])-j)/count)+j:]
                    txt[i] = '\n'.join(txt_str)
                tw, th = draw.textsize(txt[i], font=font)
                txt_img = Image.new("RGBA", (tw + 1, int(1.1*th)), (0, 0, 0, 0))
                draw = ImageDraw.Draw(txt_img)
                draw.text((0, 0), txt[i], font=font,
                          fill=(txt_color[0], txt_color[1], txt_color[2]))
                txt_img.save("txt_image/img" + str(i + 1) + ".png", "PNG")
            else:
                font = ImageFont.truetype(foo, 35 - 5 * i, encoding='utf-8')
                tw, th = draw.textsize(txt[i], font=font)
                if tw > w:
                    txt_str = txt[i].splitlines()
                    for k in range(len(txt_str)):
                        strw, strh = draw.textsize(txt_str[k], font=font)
                        if strw > w:
                            count = ceil(strw / w)
                            for j in range(count-1):
                                txt_str[k] = txt_str[k][:(j + 1) * ceil((len(txt_str[k])-j)/ count)+j] + '\n' + \
                                            txt_str[k][(j + 1) * ceil((len(txt_str[k])-j) / count)+j:]
                    txt[i] = '\n'.join(txt_str)
                tw, th = draw.textsize(txt[i], font=font)
                txt_img = Image.new("RGBA", (tw + 1, int(1.1*th)), (0, 0, 0, 0))
                draw = ImageDraw.Draw(txt_img)
                draw.text((0, 0), txt[i], font=font,
                          fill=(txt_color[0], txt_color[1], txt_color[2]))
                txt_img.save("txt_image/img" + str(i + 1) + ".png", "PNG")
    elif direction == "vertical":
        h, w, channel = img.shape

        # choose txt_color by image background
        image = Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
        bg_color = il.img_color(image)
        txt_color = [255 - bg_color[0], 255 - bg_color[1], 255 - bg_color[2]]

        # put the txt img on the bg
        draw = ImageDraw.Draw(image)
        fontpath = ["font/庞门正道标题体/庞门正道标题体2.0增强版.ttf",
                    "font/HanYiShangWeiShouShu/HYShangWeiShouShuW-1.ttf",
                    "font/ZhanKuKuaiLeTi/ZhanKuKuaiLeTi2016XiuDingBan-1.ttf",
                    "font/zhengqingke/zhengqingkehuangyou.ttf",
                    "font/siyuan/SourceHanSansSC-Bold.otf"]
        foo = choice(fontpath)

        for i in range(len(txt)):
            if i == 0:
                right = 0  # 往右位移量
                down = 0  # 往下位移量
                row_hight = 0  # 行高设置（文字行距）
                word_dir = 0;  # 文字间距
                h_count = 0
                w_count = 1
                h_count_max = 0
                font = ImageFont.truetype(foo, 80, encoding='utf-8')
                for j, s2 in enumerate(txt[i]):
                    if j == 0:
                        ww, wh = font.getsize(s2)
                        txt_img = Image.new("RGBA", (w, h),
                                            (0, 0, 0, 0))
                        draw = ImageDraw.Draw(txt_img)
                    draw.text((right, down), s2, font=font,
                              fill=(txt_color[0], txt_color[1], txt_color[2]))  # 设置位置坐标 文字 颜色 字体
                    h_count = h_count + 1
                    h_count_max = max(h_count, h_count_max)
                    if s2 == "," or s2 == "\n" or (wh*(h_count+1) > h and j+2<=len(txt[i])):  # 换行识别
                        right = right + ww + row_hight
                        down = 0
                        w_count = w_count + 1
                        h_count = 0
                        continue
                    else:
                        down = down + wh + word_dir
                roi = txt_img.crop(box=(0, 0, ww * w_count, wh * h_count_max))
                roi.save("txt_image/img" + str(i + 1) + ".png", "PNG")
            else:
                right = 0  # 往右位移量
                down = 0  # 往下位移量
                row_hight = 0  # 行高设置（文字行距）
                word_dir = 0  # 文字间距
                h_count = 0
                w_count = 1
                h_count_max = 0
                font = ImageFont.truetype(foo, 35 - 5 * i, encoding='utf-8')
                for j, s2 in enumerate(txt[i]):
                    if j == 0:
                        ww, wh = font.getsize(s2)
                        txt_img = Image.new("RGBA", (ww * len(txt[i]), wh *len(txt[i])),
                                            (0, 0, 0, 0))
                        draw = ImageDraw.Draw(txt_img)
                    draw.text((right, down), s2, font=font,
                              fill=(txt_color[0], txt_color[1], txt_color[2]))  # 设置位置坐标 文字 颜色 字体
                    h_count = h_count + 1
                    h_count_max = max(h_count, h_count_max)
                    if s2 == "," or s2 == "\n" or (wh*(h_count+1) > h and j+2<=len(txt[i])):  # 换行识别
                        right = right + ww + row_hight
                        down = 0
                        w_count = w_count + 1
                        h_count = 0
                        continue
                    else:
                        down = down + wh + word_dir
                roi = txt_img.crop(box=(0, 0, ww * w_count, wh * h_count_max))
                roi.save("txt_image/img" + str(i + 1) + ".png", "PNG")
    else:
        print("This txt direction "+direction+" is not defined!")

def addallimage(ImgPath,txtpos):
    logoPath = "logo/WechatIMG126.png"
    img = cv2.imread(ImgPath,-1)
    logoimg = cv2.imread(logoPath,-1)
    for ti in range(len(txtpos)-1):
        txt_img = cv2.imread("txt_image/img"+str(ti+1)+".png", -1)
        txth, txtw, txtchannel = txt_img.shape
        img = il.imgadd(txt_img, img, [txtpos[ti][1], txtpos[ti][0]], txth, 1080, txtpos[ti][-1])
    img = il.imgadd(logoimg,img,[txtpos[-1][1],txtpos[-1][0]], int(1080/15), 1080)
    cv2.imwrite("results/results.png", img, [int(cv2.IMWRITE_PNG_COMPRESSION), 3])

if __name__=="__main__":
    fgPath = 'foreground/WechatIMG65.png'
    txt = [u"第十八届上海国际汽车展会", u"时间：4月28日\n地点：广东省广州市开源大道232号企业加速器道232号"]
    #txt = [u"速度与激情",u"方向只有我一个\n 速度由我掌控",u"最高车速|燃油经济|操作稳定|行驶平顺"]
    bgPath = 'background/WechatIMG60.jpeg'
    imgPath, pos = choosetemplate(bgPath, fgPath, txt)
    addallimage(imgPath,pos)
