import cv2
import numpy as np
import colorsys
import PIL.Image as Image

def imgadd(fgImg, bgImg, fgPosRatio, fgSize, bgSize=3500, bgRatio=1.5):
    #read image
    img_1=fgImg
    img_2=bgImg

    #image normalizatiom
    img_1_resize=cv2.resize(img_1, (int(img_1.shape[1]*fgSize/img_1.shape[0]), fgSize), interpolation=cv2.INTER_AREA)
    img_2_resize=cv2.resize(img_2, (int(img_2.shape[1]*bgSize/img_2.shape[0]), bgSize), interpolation=cv2.INTER_AREA)


    rows, cols, channels = img_1_resize.shape
    #Pos ratio convert into Pos
    fgPos = [bgSize * fgPosRatio[0] - int(0.5 * rows), int(img_2.shape[1]*bgSize/img_2.shape[0]) * fgPosRatio[1] - int(0.5 * cols)]
    # img_text_pos=[bgSize*0.75, bgSize*bgRatio*0.8485]
    #create a ROI
    roi = img_2_resize[int(fgPos[0]):int(fgPos[0]+rows), int(fgPos[1]):int(fgPos[1]+cols)]
    #create a mask of logo and create its inverse mask
    if channels > 3:
        b,g,r,alpha = cv2.split(img_1_resize)
        img_1_resize = cv2.merge([b,g,r])
        mask = alpha
        mask_inv = cv2.bitwise_not(mask)
        # black-out the area in ROI
        img2_bg = cv2.bitwise_and(roi, roi, mask=mask_inv)

        # Take only region of foreground from foreground image.
        img1_fg = cv2.bitwise_and(img_1_resize, img_1_resize, mask=mask)
        # Put logo in ROI and modify the main image
        dst = cv2.add(img2_bg, img1_fg)
    else:
        dst = cv2.addWeighted(img_1_resize,1,roi,0,0)
    img_2_resize[int(fgPos[0]):int(fgPos[0]+rows), int(fgPos[1]):int(fgPos[1]+cols)] = dst
    return img_2_resize

#不同透明度图片叠加（还需要考虑png图像）
def addWeightedImage(foreimg, bgimg,alpha):
    h, w, channel = foreimg.shape
    img2 = cv2.resize(bgimg, (w,h), interpolation=cv2.INTER_AREA)
    #print img1.shape, img2.shape
    #alpha，beta，gamma可调
    beta = 1-alpha
    gamma = 0
    img_add = cv2.addWeighted(foreimg, alpha, img2, beta, gamma)
    return img_add

# 不透明度
def Transparent(img_1, img_2, alpha):
    img = img_1 * alpha + img_2 * (1-alpha)
    return img

# 正片叠底
def Multiply (img_1, img_2):
    img = img_1 * img_2
    return img

# 颜色加深
def Color_burn (img_1, img_2):
    img = 1 - (1 - img_2) / (img_1 + 0.001)

    mask_1 = img  < 0
    mask_2 = img  > 1

    img = img * (1-mask_1)
    img = img * (1-mask_2) + mask_2

    '''
    row, col, channel = img.shape
    for i in range(row):
        for j in range(col):
            img[i, j, 0] = min(max(img[i, j, 0], 0), 1)
            img[i, j, 1] = min(max(img[i, j, 1], 0), 1)
            img[i, j, 2] = min(max(img[i, j, 2], 0), 1)
    '''

    return img

# 颜色减淡
def Color_dodge(img_1, img_2):
    img = img_2 / (1.0 - img_1 + 0.001)
    mask_2 = img  > 1
    img = img * (1-mask_2) + mask_2
    return img

# 线性加深
def Linear_burn(img_1, img_2):
    img = img_1 + img_2 - 1
    mask_1 = img  < 0
    img = img * (1-mask_1)
    return img

# 线性减淡
def Linear_dodge(img_1, img_2):
    img = img_1 + img_2
    mask_2 = img  > 1
    img = img * (1-mask_2) + mask_2
    return img

# 变亮
def Lighten(img_1, img_2):
    img = img_1 - img_2
    mask = img > 0
    img = img_1 * mask + img_2 * (1-mask)

    return img

# 变暗
def Dark(img_1, img_2):
    img = img_1 - img_2
    mask = img < 0
    img = img_1 * mask + img_2 * (1-mask)

    return img

# 滤色
def Screen(img_1, img_2):
    img = 1- (1-img_1)*(1-img_2)

    return img

# 叠加
def Overlay(img_1, img_2):
    mask = img_2 < 0.5
    img = 2 * img_1 * img_2 * mask + (1-mask) * (1- 2 * (1-img_1)*(1-img_2))

    return img

# 柔光
def Soft_light(img_1, img_2):
    mask = img_1 < 0.5
    T1 = (2 * img_1 -1)*(img_2 - img_2 * img_2) + img_2
    T2 = (2 * img_1 -1)*(np.sqrt(img_2) - img_2) + img_2
    img = T1 * mask + T2 * (1-mask)

    return img

# 强光
def Hard_light(img_1, img_2):
    mask = img_1 < 0.5
    T1 = 2 * img_1 * img_2
    T2 = 1 - 2 * (1 - img_1) * (1 - img_2)
    img = T1 * mask + T2 * (1-mask)

    return img

# 亮光
def Vivid_light(img_1, img_2):
    mask = img_1 < 0.5
    T1 = 1 - (1 - img_2)/(2 * img_1 + 0.001)
    T2 = img_2 / (2*(1-img_1) + 0.001)
    mask_1 = T1 < 0
    mask_2 = T2 > 1
    T1 = T1 * (1-mask_1)
    T2 = T2 * (1-mask_2) + mask_2
    img = T1 * mask  + T2 * (1 - mask)

    return img

# 点光
def Pin_light(img_1, img_2):
    mask_1 = img_2 < (img_1 * 2 -1)
    mask_2 = img_2 > 2 * img_1
    T1 = 2 * img_1 -1
    T2 = img_2
    T3 = 2 * img_1
    img = T1 * mask_1 + T2 * (1 - mask_1) * (1 - mask_2) + T3 * mask_2

    return img

# 线性光
def Linear_light(img_1, img_2):
    img = img_2 + img_1 * 2 - 1
    mask_1 = img < 0
    mask_2 = img > 1
    img = img * (1-mask_1)
    img = img * (1-mask_2) + mask_2

    return img

# 实色混合
def Hard_mix(img_1, img_2):
    img = img_1 + img_2
    mask = img_1 + img_2 > 1
    img = img * (1-mask) + mask
    img = img * mask
    return img

def img_circle(img):
    # cv2.IMREAD_COLOR，读取BGR通道数值，即彩色通道，该参数为函数默认值
    # cv2.IMREAD_UNCHANGED，读取透明（alpha）通道数值
    # cv2.IMREAD_ANYDEPTH，读取灰色图，返回矩阵是两维的
    rows, cols, channel = img.shape

    # 创建一张4通道的新图片，包含透明通道，初始化是透明的
    img_new = np.zeros((rows,cols,4),np.uint8)
    img_new[:,:,0:3] = img[:,:,0:3]

    # 创建一张单通道的图片，设置最大内接圆为不透明，注意圆心的坐标设置，cols是x坐标，rows是y坐标
    img_circle = np.zeros((rows,cols,1),np.uint8)
    img_circle[:,:,:] = 0  # 设置为全透明
    img_circle = cv2.circle(img_circle,(int(cols/2),int(rows/2)),int(min(rows, cols)/2),(255),-1) # 设置最大内接圆为不透明

    # 图片融合
    img_new[:,:,3] = img_circle[:,:,0]
    img_final=img_new[int(rows/2-min(rows, cols)/2):int(rows/2+min(rows, cols)/2),int(cols/2-min(rows, cols)/2):int(cols/2+min(rows, cols)/2)]

    # 保存图片
    return img_final

def img_color(image):
    image = image.convert('RGBA')
    image.thumbnail((200, 200))
    max_score = 0.0001
    dominant_color = None
    for count, (r, g, b, a) in image.getcolors(image.size[0] * image.size[1]):
        if a == 0:
            continue
        # 转为HSV标准
        saturation = colorsys.rgb_to_hsv(r / 255.0, g / 255.0, b / 255.0)[1]
        y = min(abs(r * 2104 + g * 4130 + b * 802 + 4096 + 131072) >> 13, 235)
        y = (y - 16.0) / (235 - 16)

        # 忽略高亮色
        if y > 0.9:
            continue
        score = (saturation + 0.1) * count
        if score > max_score:
            max_score = score
            dominant_color = (r, g, b)
    return dominant_color
# img = Transparent(img_1, img_2, alpha)
# img = Multiply (img_1, img_2)
# img = Color_burn(img_1, img_2)
# img = Color_dodge(img_1, img_2)
# img = Linear_burn(img_1, img_2)
# img = Linear_dodge(img_1, img_2)
# img = Lighten(img_1, img_2)
# img = Dark (img_1, img_2)
# img = Screen(img_1, img_2)
# img = Overlay(img_1, img_2)
# img = Soft_light(img_1, img_2)
# img = Hard_light(img_1, img_2)
# img = Vivid_light(img_1, img_2)
# img = Pin_light(img_1, img_2)
# img = Linear_light(img_1, img_2)
# img = Hard_mix(img_1, image_resize)
