# FaceDetection
Machine Vision program to detect faces and anonymize detected person

## Simple README for Face and Eye Detection with Blurring Code

### Purpose:
This script does the following:
1. Detects faces in a set of images.
2. Outlines the detected faces with red bounding boxes.
3. Detects eyes within those faces.
4. Blurs the detected eye regions in the images.
5. Displays the processed images one by one.

### Description:

1. **Import Libraries**: 
   - `numpy` for numerical operations.
   - `cv2` from OpenCV for image processing and computer vision functionalities.

2. **Initialization**:
   - `image_files`: A list containing filenames of the images to be processed.
   - `pretrained`: The filename of the pre-trained Haar Cascade classifier for frontal face detection.
   - `face_cascade`: Initialize the face detection model using the pre-trained classifier.
   - `eye_cascade`: Initialize the eye detection model using the pre-trained classifier available within OpenCV.

3. **Image Processing**:
   - For each image in the `image_files` list:
     1. Read the image using OpenCV.
     2. Convert the image to grayscale for detection purposes.
     3. Detect faces in the image. For each detected face, draw a red rectangle around it.
     4. Detect eyes within the grayscale image. For each detected eye region, apply a blurring effect using the median blur method.
     5. Replace the original eye region in the image with the blurred version.

4. **Display Results**:
   - The processed image is displayed using OpenCV's `imshow`.
   - Wait for the user to press any key to close the displayed image and proceed to the next image.

### How to Use:
1. Place the images you wish to process in the appropriate directory.
2. Update the `image_files` list with the filenames of your images.
3. Ensure you have the Haar Cascade classifier (`haarcascade_frontalface_alt.xml`) in the same directory or update the path accordingly.
4. Run the script. It will process each image, detect faces and eyes, blur the eyes, and display the result. Press any key to close each displayed image and proceed to the next.
