import cv2 as cv

# img = cv.imread("Resources/Photos/cats.jpg")  # 返回像素矩阵
# cv.imshow("Cats", img)

# cv.waitKey(0)  # 设置等待时间，单位ms。0表示按键后继续执行


# 读取视频，参数是0表示读取摄像头
# capture = cv.VideoCapture(0)
capture = cv.VideoCapture("Resources/Videos/dog.mp4")

# 在读取视频时，使用while循环，每次读取一帧,读取的帧保存在frame中
# 读取成功，返回True，否则返回False，视频播放完就结束
# 或者在读取播放时按d键退出
while True:
    isTrue, frame = capture.read()
    if isTrue:
        cv.imshow("Video", frame)
        if cv.waitKey(20) & 0xFF == ord("d"):
            break
    else:
        break
# 释放捕获设备并销毁所有窗口
capture.release()
cv.destroyAllWindows()
