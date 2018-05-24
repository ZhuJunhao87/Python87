import aircv as ac


class SecurityCode(object):
    def __init__(self):
        self.x = 1

    def matchImg(imgsrc, imgobj, confidencevalue=0.5):  # imgsrc=原始图像，imgobj=待查找的图片
        imsrc = ac.imread(imgsrc)

        imobj = ac.imread(imgobj)

        match_result = ac.find_template(imsrc, imobj, confidence)
        # {'confidence': 0.5435812473297119, 'rectangle': ((394, 384), (394, 416), (450, 384), (450, 416)), 'result': (422.0, 400.0)}
        if match_result is not None:
            match_result['shape'] = (imsrc.shape[1], imsrc.shape[0])  # 0为高，1为宽
        return match_result


if __name__ == '__main__':
    print()
