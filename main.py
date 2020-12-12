import face_recognition
import os
import image_to_numpy
from shutil import copy
from logger import Logger
import cv2
import time

"""INIT"""
SOURCE_DATA = "source_dataset/"
IMAGE_SET = "images/"
FACE_FOUND_DIR = "face_found/"
TOLERANCE = 0.5
FRAME_THICKNESS = 4
COLOR = [0, 0, 255]
DETECTION_MODEL = "hog"

log = Logger()

source_faces = []

start = time.perf_counter()

"""LOADING SOURCE IMAGES"""
log.info(f"loading source images")
for index, filename in enumerate(os.listdir(SOURCE_DATA)):
    if filename.endswith("JPG"):
        log.info(f"processing source image {filename}")
        img_path = SOURCE_DATA + filename
        # using image_to_numpy to load img file -> fixes image orientation -> face encoding is found
        img = image_to_numpy.load_image_file(img_path)
        try:
            source_img_encoding = face_recognition.face_encodings(img)[0]
            log.success("face encoding found")
            source_faces.append(source_img_encoding)
        except IndexError:
            log.error("no face detected")

if len(os.listdir(SOURCE_DATA)) - len(source_faces) != 0:
    log.warn(f"{str(len(source_faces))} faces found in {str(len(os.listdir(SOURCE_DATA)))} images")

"""MAIN PROCESS"""
log.info(f"Processing dataset")
for index, filename in enumerate(os.listdir(IMAGE_SET)):
    if filename.endswith("JPG"):
        log.info(f"processing dataset image {filename} ({index + 1}/{len(os.listdir(IMAGE_SET))})")
        img_path = IMAGE_SET + filename
        img = image_to_numpy.load_image_file(img_path)
        try:
            locations = face_recognition.face_locations(img, model=DETECTION_MODEL)
            encodings = face_recognition.face_encodings(img, locations)
            for face_encoding, face_location in zip(encodings, locations):
                # for encoding in face_encodings:
                results = face_recognition.compare_faces(source_faces, face_encoding, TOLERANCE)
                if True in results:
                    log.success("match found!")
                    top_left = (face_location[3], face_location[0])
                    bottom_right = (face_location[1], face_location[2])
                    cv2.rectangle(img, top_left, bottom_right, COLOR, FRAME_THICKNESS)
                    cv2.imwrite(FACE_FOUND_DIR + "_" + filename, img)
                    copy(img_path, FACE_FOUND_DIR)
                    break
                else:
                    log.warn("no match found")
        except IndexError:
            log.error("no face detected")
        except Exception as err:
            log.error(f"error encountered: {err}")

stop = time.perf_counter()

print(f"Total time taken was {stop - start:0.4f} seconds")
