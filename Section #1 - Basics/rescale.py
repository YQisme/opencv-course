import cv2 as cv


capture = cv.VideoCapture("Resources/Videos/dog.mp4")

while True:
    isTrue, frame = capture.read()
    # cv.resize()，需要传入图像数组，目标的宽高元组，以及插值方法
    # 图像或者视频帧的属性shape[0]是高，shape[1]是宽
    # 插值方法：cv.INTER_AREA - 用于缩小图像，cv.INTER_CUBIC - 用于放大图像，cv.INTER_LINEAR - 用于缩小或放大图像
    frame_resized = cv.resize(
        frame,
        (int(frame.shape[1] * 0.5), int(frame.shape[0] * 0.5)),
        interpolation=cv.INTER_AREA,
    )
    if isTrue:
        cv.imshow("Video", frame)
        cv.imshow("Video Resized", frame_resized)
        if cv.waitKey(20) & 0xFF == ord("d"):
            break
    else:
        break

capture.release()
cv.destroyAllWindows()
