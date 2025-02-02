import cv2
import time
import datetime
import os


def take_photo_now():
    """take_photo_now is code to take a photo immediately"""
    try:
        # try to make the folder
        os.mkdir("static")
        os.mkdir("static/Data")
        os.makedirs("static/Compressed")
    except Exception as e:
        # folder already exists
        pass

    # change folder
    os.chdir("/home/pi/Lab-Partner/static/Data")

    # reading the camera
    cam = cv2.VideoCapture(0)
    ret_val, img = cam.read()

    # generate filename
    now = datetime.datetime.now()
    filename = now.strftime("%Y_%m_%d-%H_%M_%S") + ".png"

    # save image
    cv2.imwrite(filename, img)

    # compress image
    os.chdir("/home/pi/Lab-Partner/static/Compressed")
    compressed_path = filename
    compression_rate = [cv2.IMWRITE_JPEG_QUALITY, 50]
    cv2.imwrite(compressed_path, img, compression_rate)

    # releasing the camera
    cam.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    take_photo_now()
