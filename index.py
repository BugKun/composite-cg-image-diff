import os
from PIL import Image
from shutil import copyfile


inputDirPath = ''
outputDirPath = ''
diffDirPath = ''
targetExtname = '.png'

# 效果不理想，推荐使用potoshop批处理，选择黑色部分删除，然后羽化或收缩去除边缘锯齿
def replaceColorToTransparent(img, r, g, b):
    datas = img.getdata()
    newData = []
    for item in datas:
        if item[0] == r and item[1] == g and item[2] == b:
            newData.append((255, 255, 255, 0))
        else:
            newData.append(item)
    img.putdata(newData)
    return img


def changePosition(img, x, y):
    result = Image.new(mode="RGBA", size=img.size)
    result.paste(img, (x, y))
    return result

def filterDiff(each, filename):
    return filename in each
    

if __name__ == '__main__':
    sourceList = list(filter(lambda each: os.path.isfile(os.path.join(inputDirPath, each)), os.listdir(inputDirPath)))
    sourceListLen = len(sourceList)
    print('共%d个图片待处理' % (sourceListLen))
    for sourceIndex, source in enumerate(sourceList):
        filePath = os.path.join(inputDirPath, source)
        filename, extname = os.path.splitext(source)
        diffList = list(filter(lambda each: filterDiff(each, filename), os.listdir(diffDirPath)))
        diffListLen = len(diffList)
        if extname == targetExtname:
            print('正在复制第%d个图片的原始图片' % (sourceIndex + 1))
            copyfile(filePath, os.path.join(outputDirPath, source))
        else:
            print('正在转换第%d个图片的原始图片为%s格式' % (sourceIndex + 1, targetExtname))
            Image.open(filePath).convert('RGB').save(os.path.join(outputDirPath, filename + targetExtname))
        background = Image.open(filePath).convert('RGBA')
        print('共有%d个差分图片待处理' % (diffListLen))
        for diffIndex, diff in enumerate(diffList):
            print('正在处理第(%d/%d)个图片的第(%d/%d)个差分图片' % (sourceIndex + 1, sourceListLen, diffIndex + 1, diffListLen))
            foreground = Image.open(os.path.join(diffDirPath, diff)).convert('RGBA')
            diffname = os.path.splitext(diff)[0]
            Image.alpha_composite(background, foreground).convert('RGB').save(os.path.join(outputDirPath, diffname + targetExtname))


