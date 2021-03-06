# Document scanner filter


## Introduction
---

### So what is Document scanner? 
Document scanner is a simple image enhancement technique that attempts to improve the sharpness in an image followed by 
increasing the colour saturation level, improvinng the intensity of white colour pixels in the image (also whitening the yellow image pixels), 
and finally normalizing the complete image colours to give us a filter that improves text visibility on the document image.

**Note:** *The whitening intensity can be changed by playing with the `value` in method `whitebalance()` [default setting `value = 125`]*

## Running
---

Run the following code:
```shell
python3 scanner.py
```

## Process
---

The algorithm, works pixel by pixel changing intensities of every pixel in order to get a more enhanced image. It works as shown in the below figures.

The original input image:

![image](https://user-images.githubusercontent.com/30645315/49373114-e358da80-f722-11e8-9b43-c4c63fff4431.jpg)


The enhanced image generated by the algorithm:

![normalizedimage](https://user-images.githubusercontent.com/30645315/49372820-ddaec500-f721-11e8-8fc9-51ff329da3b6.jpg)


## Links
---

- Project homepage: https://github.com/johri002/OpenCv-Projects/tree/master/Scanner%20filter
- Repository: https://github.com/johri002/OpenCv-Projects
- Issue tracker: https://github.com/johri002/OpenCv-Projects/issues
