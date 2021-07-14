# composite-cg-image-diff

CG图片基础合成工具。

## 介绍

现在，有很多游戏厂商为了减少封装的体积，会使用差分技术来储存CG图片，导致CG不能很方便的被提取，需要自己合成。

合成的规则可能是简单的图片合成，也有可能是要根据读取相关配置文件，按照一定的规则进行合成。也有些时候是因为技术原因，我们只能在网上下载别人提取好的CG。

但部分CG没有被保存成支持透明通道的图片格式，导致无法很好的合成差分文件，我尝试用`Pillow`来简单处理这样的文件，但效果不理想，这种情况我还是推荐使用Photoshop的动作功能来批量处理图片。

`Pillow`处理的方式如下：

```python
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
```

[English version](readme.en.md)