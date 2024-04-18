import uuid
from flask import *
from database import*
import os

police_staff=Blueprint('police_staff',__name__)



@police_staff.route('/staffhome')
def staff_home():
    return render_template("staff_home.html")



@police_staff.route('/staff_profile')
def staff_profile():
    data={}
    qry="select * from staff inner join station using(station_id) where staff_id='%s'"%(session['staff'])
    res=select(qry)
    if res:
        data['view']=res
    return render_template("staff_profile.html",data=data)



@police_staff.route('/staff_viewcase',methods=['get','post'])
def staff_viewcase():
    data={}
    qry="select * from assigned_cases inner join registered_cases using(case_id) where staff_id='%s'"%(session['staff'])
    res=select(qry)
    if res:
        data['view']=res
        
    if'action'in request.args:
        action=request.args['action']
        id=request.args['id']
        
        if action=='case_status':
            qry1="select * from assigned_cases where assign_id='%s'"%(id)
            res1=select(qry1)
            data['details']=res1
            
            if 'submit' in request.form:
                description=request.form['description']
                
                qry2="insert into case_status values(null,'%s','%s',curdate())"%(id,description)
                insert(qry2)
                return ("<script>alert('CASE STATUS ADDED');window.location='/staff_viewcase'</script>")

    return render_template("staff_viewcase.html",data=data)




@police_staff.route('/view_case_status')
def view_case_status():
    id=request.args['id']
    data={}
    qry="select * from case_status where assigned_id='%s'"%(id)
    res=select(qry)
    if res:
        data['view']=res
    return render_template("view_case_status.html",data=data)



@police_staff.route('/staff_com',methods=['get','post'])
def staff_com():
    data={}
    qry1="select * from complaints where sender_id='%s'"%(session['log'])
    res1=select(qry1)
    print(res1,"ppppppppppppppppppppp")
    if res1:
        data['view']=res1
    if'submit' in request.form:
        title=request.form['title']
        description=request.form['description']
        qry="insert into complaints values(null,'%s','%s','%s','pending',curdate())"%(session['log'],title,description)
        insert(qry)
        return ("<script>alert('COMPLAINT SEND');window.location='/staff_com'</script>")

    return render_template("staff_complaints.html",data=data)


# from core import *
# from predict import pred
# from skimage.metrics import structural_similarity as ssim
# @police_staff.route('/add_evidence',methods=['get','post'])
# def add_evidence():
#     if'submit' in request.form:
#         id=request.args['id']
#         file=request.files['evidence']
#         qre="select case_id from assigned_cases where assign_id='%s'"%(id)
#         re=select(qre)
        
#         qry="insert into evidences values(null,(select case_id from assigned_cases where assign_id='%s'),'pending','ADDED')"%(id)
#         res=insert(qry)
#         ev_id=str(res)
#         pid=str(re[0]['case_id'])
#         isFile = os.path.isdir("static/evidences/"+pid)  
#         print(isFile)
#         if(isFile==False):
#             os.mkdir('static\\evidences\\'+pid)
#         path="static/evidences/"+pid+"/"+str(uuid.uuid4())+file.filename
#         file.save(path)
#         qr="update evidences set file='%s' where evidence_id='%s'"%(path,ev_id)
#         update(qr)
#         enf("static/evidences/")
#         value=pred(path)
#         print(value,"______________________________")
#         if value=='Crime Evidence':
#             # result=val(path)
#             # print(result,"++++++++++++++++++++++++")
            
#             nparr = np.fromstring(file.read(), np.uint8)
#             path = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

#             # Compare uploaded image with stored images
#             best_match = compare_images(path, data)
#             print(best_match,"pppppppppppppppppppp")


            
#     return render_template("staff_Add_evidences.html")


# data = pickle.loads(open('faces.pickles', "rb").read())

# def compare_images(path, data):
#     best_match = None
#     max_similarity = -1
#     for filename, encoded_image in data.items():
#         similarity = ssim(path, encoded_image)
#         if similarity > max_similarity:
#             max_similarity = similarity
#             best_match = filename
#     return best_match




from core import *
from predict import pred
from skimage.metrics import structural_similarity as ssim
import cv2
import numpy as np
import os
import uuid





# @police_staff.route('/add_evidence', methods=['GET', 'POST'])
# def add_evidence():
#     if 'submit' in request.form:
#         id = request.args['id']
#         file = request.files['evidence']
#         qre = "select case_id from assigned_cases where assign_id='%s'" % id
#         re = select(qre)
        
#         qry = "insert into evidences values(null, (select case_id from assigned_cases where assign_id='%s'), 'pending', 'ADDED')" % id
#         res = insert(qry)
#         ev_id = str(res)
#         pid = str(re[0]['case_id'])
#         isFile = os.path.isdir("static/evidences/" + pid)  
#         print(isFile)
#         if not isFile:
#             os.mkdir('static\\evidences\\' + pid)
#         path = "static/evidences/" + pid + "/" + str(uuid.uuid4()) + file.filename
#         file.save(path)
#         qr = "update evidences set file='%s' where evidence_id='%s'" % (path, ev_id)
#         update(qr)
#         enf("static/evidences/")
#         value = pred(path)
#         print(value, "______________________________")
#         data = pickle.loads(open('uploaded_images.pickles', "rb").read())
#         print(data,"yyyyyyyyyyyyyyy")
#         if value == 'Crime Evidence':
#             best_match = compare_images(path, data)
#             print(best_match, "pppppppppppppppppppp")

#     return render_template("staff_Add_evidences.html")

# def compare_images(path, data):
#     best_match = None
#     max_similarity = -1
#     image = cv2.imread(path)
#     for filename, encoded_image in data.items():
#         similarity = ssim(image, encoded_image)
#         if similarity > max_similarity:
#             max_similarity = similarity
#             best_match = filename
#     return best_match



import cv2
import os
import pickle
import uuid
import numpy as np
from flask import request, render_template
from core import select, insert, update, enf
from predict import pred
from skimage.metrics import structural_similarity as ssim
from scipy.spatial.distance import cosine

@police_staff.route('/add_evidence', methods=['GET', 'POST'])
def add_evidence():
    value={}
    if 'submit' in request.form:
        id = request.args['id']
        file = request.files['evidence']
        qre = "select case_id from assigned_cases where assign_id='%s'" % id
        re = select(qre)
        
        qry = "insert into evidences values(null, (select case_id from assigned_cases where assign_id='%s'), 'pending', 'ADDED')" % id
        res = insert(qry)
        ev_id = str(res)
        pid = str(re[0]['case_id'])
        isFile = os.path.isdir("static/evidences/" + pid)  
        print(isFile)
        if not isFile:
            os.mkdir('static/evidences/' + pid)
        path = "static/evidences/" + pid + "/" + str(uuid.uuid4()) + file.filename
        file.save(path)
        qr = "update evidences set file='%s' where evidence_id='%s'" % (path, ev_id)
        update(qr)
        enf("static/evidences/")###function
        val = pred(path)###function
        print(val, "______________________________")
        data = pickle.loads(open('uploaded_images.pickles', "rb").read())
       
        print("*******************************")
        print(data, "yyyyyyyyyyyyyyy")
        if val == 'Crime Evidence':
            best_folder_name = compare_images(path, data)

            print(best_folder_name, "pppppppppppppppppppp")
            all_results = []  # Use a list to temporarily store dictionaries

            for case_id in best_folder_name:
                qry3 = "select * from registered_cases inner join station using(station_id)  where case_id='%s'" % (case_id)
                res3 = select(qry3)
                for result in res3:
                    if result not in all_results:  # Check if the dictionary is not already in the list
                        all_results.append(result)  # Add dictionary to list
                        print(all_results,"pppppppppp")

            # return all_results
            value = {'view': all_results} 
        return render_template("staff_Add_evidences.html",value=value,val=val)
                        
                        
                                                

    return render_template("staff_Add_evidences.html",value=value)





# def compare_images(path, data):
#     best_match = None
#     max_similarity = -1
#     image = cv2.imread(path)
#     image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)  # Convert to RGB for SSIM comparison

#     for encoded_image in data['encodings']:
#         encoded_image = cv2.cvtColor(encoded_image, cv2.COLOR_BGR2RGB)  # Convert to RGB for SSIM comparison

#         # Resize the images to a common size for comparison
#         resized_image = cv2.resize(image, (encoded_image.shape[1], encoded_image.shape[0]))

#         try:
#             # Perform similarity comparison between the resized images
#             similarity = ssim(resized_image, encoded_image, multichannel=True, win_size=min(resized_image.shape))
#         except ZeroDivisionError:
#             continue  # Skip this comparison if ZeroDivisionError occurs

#         # Update 'best_match' and 'max_similarity' accordingly
#         if not np.isnan(similarity) and not np.isinf(similarity) and similarity != 1.0 and similarity != -1.0:
#             if similarity > max_similarity:
#                 max_similarity = similarity
#                 best_match = encoded_image  # Assuming encoded_image is the filename or identifier

#     return best_match


#############corrected code
# def compare_images(path, data):
#     best_match = None
#     max_similarity = -1
#     image = cv2.imread(path)
#     image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)  # Convert to RGB for SSIM comparison

#     for encoded_image in data['encodings']:
#         # Convert encoded_image to RGB and resize it to match the size of the image at path
#         encoded_image = cv2.cvtColor(encoded_image, cv2.COLOR_BGR2RGB)
#         resized_encoded_image = cv2.resize(encoded_image, (image.shape[1], image.shape[0]))

#         # Perform similarity comparison between the resized images
#         try:
#             similarity = ssim(image, resized_encoded_image, multichannel=True, win_size=min(image.shape))
#         except ZeroDivisionError:
#             continue  # Skip this comparison if ZeroDivisionError occurs

#         # Update 'best_match' and 'max_similarity' accordingly
#         if not np.isnan(similarity) and not np.isinf(similarity) and similarity != 1.0 and similarity != -1.0:
#             if similarity > max_similarity:
#                 max_similarity = similarity
#                 best_match = encoded_image  # Assuming encoded_image is the filename or identifier

#     return best_match


# def compare_images(path, data):
#     best_match_name = None
#     max_similarity = -1
#     image = cv2.imread(path)
#     image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)  # Convert to RGB for SSIM comparison

#     for i, encoded_image in enumerate(data['encodings']):
#         # Convert encoded_image to RGB and resize it to match the size of the image at path
#         encoded_image = cv2.cvtColor(encoded_image, cv2.COLOR_BGR2RGB)
#         resized_encoded_image = cv2.resize(encoded_image, (image.shape[1], image.shape[0]))

#         # Perform similarity comparison between the resized images
#         try:
#             similarity = ssim(image, resized_encoded_image, multichannel=True, win_size=min(image.shape))
#         except ZeroDivisionError:
#             continue  # Skip this comparison if ZeroDivisionError occurs

#         # Update 'best_match_name' and 'max_similarity' accordingly
#         if not np.isnan(similarity) and not np.isinf(similarity) and similarity != 1.0 and similarity != -1.0:
#             if similarity > max_similarity:
#                 max_similarity = similarity
#                 best_match_name = data['names'][i]  # Assuming names are stored in data['names']

#     return best_match_name



# def compare_images(path, data):
#     best_matches = []
#     image = cv2.imread(path)
#     image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)  # Convert to RGB for SSIM comparison

#     for i, encoded_image in enumerate(data['encodings']):
#         # Convert encoded_image to RGB and resize it to match the size of the image at path
#         encoded_image = cv2.cvtColor(encoded_image, cv2.COLOR_BGR2RGB)
#         resized_encoded_image = cv2.resize(encoded_image, (image.shape[1], image.shape[0]))

#         # Perform similarity comparison between the resized images
#         try:
#             similarity = ssim(image, resized_encoded_image, multichannel=True, win_size=min(image.shape))
#         except ZeroDivisionError:
#             continue  # Skip this comparison if ZeroDivisionError occurs

#         print(f"Similarity with image {data['names'][i]}: {similarity}")

#         # Check if the similarity is within an acceptable range
#         if not np.isnan(similarity) and not np.isinf(similarity) and similarity != 1.0 and similarity != -1.0:
#             # Append the name of the encoded image to the list of best matches
#             best_matches.append(data['names'][i])
#             print(f"Added {data['names'][i]} to best matches.")

#     print("Best matches:", best_matches)
#     return best_matches


# def compare_images(path, data, threshold=0.3):
#     best_matches = []
#     image = cv2.imread(path)
#     image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)  # Convert to RGB for SSIM comparison

#     for i, encoded_image in enumerate(data['encodings']):
#         # Convert encoded_image to RGB and resize it to match the size of the image at path
#         encoded_image = cv2.cvtColor(encoded_image, cv2.COLOR_BGR2RGB)
#         resized_encoded_image = cv2.resize(encoded_image, (image.shape[1], image.shape[0]))

#         # Perform similarity comparison between the resized images
#         try:
#             similarity = ssim(image, resized_encoded_image, multichannel=True)
#         except ValueError as e:
#             print(f"Error comparing images: {e}")
#             continue

#         print(f"Similarity with image {data['names'][i]}: {similarity}")
#         print(threshold,"000000000000000000")

#         # Check if the similarity exceeds the threshold
#         if similarity >= threshold:
#             # Append the name of the encoded image to the list of best matches
#             best_matches.append(data['names'][i])
#             print(f"Added {data['names'][i]} to best matches.")

#     print("Best matches:", best_matches)
#     return best_matches

import cv2
import numpy as np

def compare_images(path, data, threshold=15000):
    best_matches = []
    try:
        # Read the uploaded image
        uploaded_image = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
        if uploaded_image is None:
            raise ValueError("Failed to read the uploaded image")

        # Ensure data contains encodings and names
        if 'encodings' not in data or 'names' not in data:
            raise ValueError("Invalid data format. 'encodings' and 'names' must be present in the data dictionary")

        # Check if there are any encoded images
        if len(data['encodings']) == 0:
            raise ValueError("No encoded images found in the data")

        print("Uploaded image shape:", uploaded_image.shape)

        # Reshape the uploaded image to a 1D array
        uploaded_image_1d = uploaded_image.flatten()
        
        uploaded_image_shape = (207000,)
        uploaded_image_1d = np.zeros(uploaded_image_shape)  # This is a placeholder, replace it with your actual image data

        # Reshape the uploaded image to match the encoded image shape
        flattened_image = uploaded_image_1d[:30000]


        # Loop through each encoded image
        for i, encoded_image in enumerate(data['encodings']):
            
            print(f"Encoded image shape for {data['names'][i]}:", encoded_image.shape)

            # Check if the shapes match
            if encoded_image.shape != flattened_image.shape:
                print(f"Skipping comparison with image {data['names'][i]}: Shape mismatch")
                continue

            # Calculate MSE
            mse = np.mean((encoded_image - flattened_image) ** 2)
            print(f"MSE with image {data['names'][i]}: {mse}")

            # Check if MSE is below the threshold
            if mse <= threshold:
                best_matches.append(data['names'][i])
                print(f"Added {data['names'][i]} to best matches.")

    except Exception as e:
        print(f"Error occurred: {e}")

    print("Best matches:", best_matches)
    return best_matches





@police_staff.route('/crime_image')
def crime_image():
    data={}
    id=request.args['id']
    qry="select * from evidences where case_id='%s'"%(id)
    res=select(qry)
    if res:
        data['view']=res
    return render_template("view_evidences.html",data=data)




# import cv2
# from skimage.metrics import structural_similarity as ssim

# def compare_images(path, data, threshold=0.3):
#     best_matches = []
#     try:
#         image = cv2.imread(path)
#         if image is None:
#             raise ValueError("Failed to read the uploaded image")

#         image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)  # Convert to RGB for SSIM comparison

#         print("Uploaded image shape:", image.shape)

#         for i, encoded_image in enumerate(data['encodings']):
#             # Convert encoded_image to RGB and resize it to match the size of the image at path
#             encoded_image = cv2.cvtColor(encoded_image, cv2.COLOR_BGR2RGB)
#             resized_encoded_image = cv2.resize(encoded_image, (image.shape[1], image.shape[0]))

#             # Print resized encoded image shape for debugging
#             print(f"Resized encoded image shape for {data['names'][i]}:", resized_encoded_image.shape)

#             # Perform similarity comparison between the resized images
#             similarity = ssim(image, resized_encoded_image, multichannel=True)

#             # Debug: Print similarity scores for debugging
#             print(f"Similarity with image {data['names'][i]}: {similarity}")

#             # Check if the similarity exceeds the threshold
#             if similarity >= threshold:
#                 # Append the name of the encoded image to the list of best matches
#                 best_matches.append(data['names'][i])
#                 print(f"Added {data['names'][i]} to best matches.")

#     except Exception as e:
#         print(f"Error occurred: {e}")

#     print("Best matches:", best_matches)
#     return best_matches



@police_staff.route('/view_crime_images')
def view_crime_images():
    data={}
    id=request.args['id']
    qry="select * from evidences inner join registered_cases using(case_id) where case_id='%s'"%(id)
    res=select(qry)
    if res:
        data['view']=res
    return render_template("view_crime_images.html",data=data)