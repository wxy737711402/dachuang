from matplotlib import pyplot as plt
import numpy as np
import cv2 as cv


def LBP_Cal(src):
    dst = np.zeros(src.shape,dtype = src.dtype)
    #src.shape读取矩阵数组  dtype数组数字类型
    for row in range(1,src.shape[0]-1):
        #行循环
        for col in range(1,src.shape[1]-1):
            #列循环
            center = src[row,col]
            LBPtemp = 0

            LBPtemp |= (src[row-1,col-1] >= center) << 7
            LBPtemp |= (src[row-1,col  ] >= center) << 6
            LBPtemp |= (src[row-1,col+1] >= center) << 5
            LBPtemp |= (src[row  ,col-1] >= center) << 4
            LBPtemp |= (src[row  ,col+1] >= center) << 3
            LBPtemp |= (src[row+1,col-1] >= center) << 2
            LBPtemp |= (src[row+1,col  ] >= center) << 1
            LBPtemp |= (src[row+1,col+1] >= center) << 0
            dst[row,col] = LBPtemp

    return dst

def main():
    src_ori = cv.imread("1.jpg")
    src = cv.cvtColor(src_ori,cv.COLOR_RGB2GRAY)
    dst = LBP_Cal(src)
    cv.imwrite("lbp_dst.jpg",dst)

    rate = np.zeros((1,256))
    for row in range(0,dst.shape[0]-1):
        for col in range(0,dst.shape[1]-1):
            rate[0,dst[row,col]] = rate[0,dst[row,col]] + 1

    np.save("rates.npy",rate)
    np.save("LBPs.npy",dst)

if __name__ == '__main__':
    main()
