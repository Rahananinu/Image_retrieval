# import tensorflow as tf
# from tensorflow.keras.models import load_model
# from tensorflow.keras.preprocessing import image
# import numpy as np

# def pred(path):

#     # Load the saved model
#     model = load_model('new_latestcrime_classifier_model.h5')

#     # Function to preprocess the uploaded image
#     def preprocess_image(image_path):
#         img = image.load_img(image_path, target_size=(150, 150))
#         img_array = image.img_to_array(img)
#         img_array = np.expand_dims(img_array, axis=0)
#         return img_array

#     # Function to classify the image
#     def classify_image(image_path):
#         img_array = preprocess_image(image_path)
#         prediction = model.predict(img_array)
#         print(prediction[0])
#         if prediction[0] > 0.5:
#             return "Crime Evidence"
#         else:
#             return "Non-Crime Evidence"

#     # Example usage
#     uploaded_image_path = 'C:\\project_check\\image\\dataset\\Non_crime_evidence\\0\\0_1.jpg'
#     result = classify_image(path)
#     print("Result:", result)
#     return str(result)



####################new#############




import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.vgg16 import preprocess_input
import numpy as np

def pred(path):
    # Load the saved model
    model = load_model('new_latest_crime_classifier_model.h5')

    # Function to preprocess the uploaded image
    def preprocess_image(image_path):
        img = image.load_img(image_path, target_size=(100, 100))  # Load image with target size
        img_array = image.img_to_array(img)  # Convert image to array
        img_array = preprocess_input(img_array)  # Preprocess the image array
        return img_array

    # Function to classify the image
    def classify_image(image_path):
        img_array = preprocess_image(image_path)  # Preprocess the uploaded image
        img_array = tf.expand_dims(img_array, axis=0)  # Add batch dimension
        # Predict using the model
        prediction = model.predict(img_array)
        print(prediction[0])
        if prediction[0] >= 0.5:  # Use greater or equal to ensure correct prediction
            return "Crime Evidence"
        else:
            return "Non-Crime Evidence"

    # Example usage
    uploaded_image_path = 'C:\\project_check\\new_image\\dataset\\crime_evidence\\Copy-of-Untitled-Design-66 - Copy - Copy (2) - Copy.png'
    result = classify_image(path)
    print("Result:", result)
    return result


