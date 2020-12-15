# FindMyFace
Face recognition experiment using `face_recognition`, `image_to_numpy` and `OpenCV2`. 
For a better understanding of why this project was created and how it works, please read the following article: [A Story of Face Recognition using Python](https://dev.to/hamza5485/a-story-of-face-recognition-using-python-3b1a).

## Directory/Files Explanation
+ `main.py` contains the core of this project.
+ `logger.py` is a simple logger service that prints out colored logs based on message severity. [You can check it out here!](https://github.com/hamza5485/PythonLogger)
+ `images` directory contains all the images in `.JPG` format.
+ `source_dataset` directory contains sample images of the person whose face needs to be searched, in `.JPG` format.
+ `face_found` directory is an image dropbox for the search results. 

## Code Flow
The program first iterates through the `source_dataset` directory. For each image in the directory, the face encodings are extracted and stored inside an array. Let's call these **"Known Faces"**. The code then proceeds to iterate through the `images` directory. For each image, the face locations of each face are extracted. These locations are then used to extract the face encodings of each face. Let's call these **"Unknown Faces"**. Each unknown face will now be compared against all the known faces to determine whether there is any similarity. If a similarity exists, the image will be stored inside the `face_found` directory. 
