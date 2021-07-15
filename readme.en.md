# composite-cg-image-diff

An CG image composite tool with basic function.

## Introduction

Nowadays, there are many game manufacturers using differential technology to store CG images in order to reduce the size of the package, resulting in CG images that can't be extracted conveniently and had to be composited by self.

The rules of composite may be composite picture simply, or may be needed to according the configuration file to composite CG images. In addition, for some technical reasons, we can only download CG images which extracted by others on the Internet.

But sometimes part of the CG images are not saved as picture format that supports transparent channels, in order to hard to composite differential images. Although, I had tried to use `Pillow` to simply recover such files, but the results were always not satisfactory, so that in this case I recommend using Photoshop's action function to batch recover differential images.

The recover function is as follows:

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

## Usage
Modify the code of `index.py` according to the actual situation, and then run it.
```bash
python3 index.py
```

[中文说明](readme.md)