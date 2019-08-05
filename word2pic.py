import pygame
import cv2
import PIL.Image as Image


def transparent_back(img):
    img = img.convert('RGBA')
    L, H = img.size
    color_0 = img.getpixel((0, 0))
    for h in range(H):
        for l in range(L):
            dot = (l, h)
            color_1 = img.getpixel(dot)
            if color_1 == color_0:
                color_1 = color_1[:-1] + (0,)
                img.putpixel(dot, color_1)
    return img


if __name__ == '__main__':
    pygame.init()
    text = u"你好"

    # all_fonts = pygame.font.get_fonts()
    # print(all_fonts)
    font = pygame.font.SysFont('/Library/Fonts/Marion.ttf', 64)
    # ftext = font.render(text, True, (65, 83, 130), (255, 255, 255))
    ftext = font.render(text, True, (255, 0, 255))
    cv2.imshow(ftext,"imshow")

    # img = Image.open('image.jpg')
    # img = transparent_back(img)
    # img.save('img_trans.png')
