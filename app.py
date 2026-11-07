# from flask import Flask, render_template,request,redirect,send_from_directory,url_for
# import numpy as np
# import json
# import uuid
# import tensorflow as tf

# app = Flask(__name__)
# model = tf.keras.models.load_model("models/Plant_disease_recog_model_pwp.keras")
# label = ['Apple___Apple_scab',
#  'Apple___Black_rot',
#  'Apple___Cedar_apple_rust',
#  'Apple___healthy',
#  'Background_without_leaves',
#  'Blueberry___healthy',
#  'Cherry___Powdery_mildew',
#  'Cherry___healthy',
#  'Corn___Cercospora_leaf_spot Gray_leaf_spot',
#  'Corn___Common_rust',
#  'Corn___Northern_Leaf_Blight',
#  'Corn___healthy',
#  'Grape___Black_rot',
#  'Grape___Esca_(Black_Measles)',
#  'Grape___Leaf_blight_(Isariopsis_Leaf_Spot)',
#  'Grape___healthy',
#  'Orange___Haunglongbing_(Citrus_greening)',
#  'Peach___Bacterial_spot',
#  'Peach___healthy',
#  'Pepper,_bell___Bacterial_spot',
#  'Pepper,_bell___healthy',
#  'Potato___Early_blight',
#  'Potato___Late_blight',
#  'Potato___healthy',
#  'Raspberry___healthy',
#  'Soybean___healthy',
#  'Squash___Powdery_mildew',
#  'Strawberry___Leaf_scorch',
#  'Strawberry___healthy',
#  'Tomato___Bacterial_spot',
#  'Tomato___Early_blight',
#  'Tomato___Late_blight',
#  'Tomato___Leaf_Mold',
#  'Tomato___Septoria_leaf_spot',
#  'Tomato___Spider_mites Two-spotted_spider_mite',
#  'Tomato___Target_Spot',
#  'Tomato___Tomato_Yellow_Leaf_Curl_Virus',
#  'Tomato___Tomato_mosaic_virus',
#  'Tomato___healthy']

# with open("plant_disease.json",'r') as file:
#     plant_disease = json.load(file)

# # print(plant_disease[4])

# @app.route('/uploadimages/<path:filename>')
# def uploaded_images(filename):
#     return send_from_directory('./uploadimages', filename)

# @app.route('/',methods = ['GET'])
# def home():
#     return render_template('home.html')

# def extract_features(image):
#     image = tf.keras.utils.load_img(image,target_size=(160,160))
#     feature = tf.keras.utils.img_to_array(image)
#     feature = np.array([feature])
#     return feature

# def model_predict(image):
#     img = extract_features(image)
#     prediction = model.predict(img)
#     # print(prediction)
#     prediction_label = plant_disease[prediction.argmax()]
#     return prediction_label

# @app.route('/upload/',methods = ['POST','GET'])
# def uploadimage():
#     if request.method == "POST":
#         image = request.files['img']
#         temp_name = f"uploadimages/temp_{uuid.uuid4().hex}"
#         image.save(f'{temp_name}_{image.filename}')
#         print(f'{temp_name}_{image.filename}')
#         prediction = model_predict(f'./{temp_name}_{image.filename}')
#         return render_template('home.html',result=True,imagepath = f'/{temp_name}_{image.filename}', prediction = prediction )

#     else:
#         return redirect('/')


# if __name__ == "__main__":
#     app.run(debug=True)


# Second code base ----------------------------------------------------
# from flask import Flask, render_template, request, redirect, send_from_directory, url_for
# import numpy as np
# import json
# import uuid
# import tensorflow as tf

# app = Flask(__name__)
# model = tf.keras.models.load_model("models/Plant_disease_recog_model_pwp.keras")

# label = [
#     'Apple___Apple_scab',
#     'Apple___Black_rot',
#     'Apple___Cedar_apple_rust',
#     'Apple___healthy',
#     'Background_without_leaves',
#     'Blueberry___healthy',
#     'Cherry___Powdery_mildew',
#     'Cherry___healthy',
#     'Corn___Cercospora_leaf_spot Gray_leaf_spot',
#     'Corn___Common_rust',
#     'Corn___Northern_Leaf_Blight',
#     'Corn___healthy',
#     'Grape___Black_rot',
#     'Grape___Esca_(Black_Measles)',
#     'Grape___Leaf_blight_(Isariopsis_Leaf_Spot)',
#     'Grape___healthy',
#     'Orange___Haunglongbing_(Citrus_greening)',
#     'Peach___Bacterial_spot',
#     'Peach___healthy',
#     'Pepper,_bell___Bacterial_spot',
#     'Pepper,_bell___healthy',
#     'Potato___Early_blight',
#     'Potato___Late_blight',
#     'Potato___healthy',
#     'Raspberry___healthy',
#     'Soybean___healthy',
#     'Squash___Powdery_mildew',
#     'Strawberry___Leaf_scorch',
#     'Strawberry___healthy',
#     'Tomato___Bacterial_spot',
#     'Tomato___Early_blight',
#     'Tomato___Late_blight',
#     'Tomato___Leaf_Mold',
#     'Tomato___Septoria_leaf_spot',
#     'Tomato___Spider_mites Two-spotted_spider_mite',
#     'Tomato___Target_Spot',
#     'Tomato___Tomato_Yellow_Leaf_Curl_Virus',
#     'Tomato___Tomato_mosaic_virus',
#     'Tomato___healthy'
# ]

# with open("plant_disease.json", 'r') as file:
#     plant_disease = json.load(file)

# @app.route('/uploadimages/<path:filename>')
# def uploaded_images(filename):
#     return send_from_directory('./uploadimages', filename)

# @app.route('/', methods=['GET'])
# def home():
#     return render_template('home.html')

# @app.route('/about', methods=['GET'])
# def about():
#     return render_template('about.html')

# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         # Add your authentication/session handling here
#         return redirect(url_for('home'))
#     return render_template('login.html')

# @app.route('/signup', methods=['GET', 'POST'])
# def signup():
#     if request.method == 'POST':
#         # Add your user registration/database logic here
#         return redirect(url_for('login'))
#     return render_template('signup.html')

# def extract_features(image):
#     image = tf.keras.utils.load_img(image, target_size=(160, 160))
#     feature = tf.keras.utils.img_to_array(image)
#     feature = np.array([feature])
#     return feature

# def model_predict(image):
#     img = extract_features(image)
#     prediction = model.predict(img)
#     prediction_label = plant_disease[prediction.argmax()]
#     return prediction_label

# @app.route('/upload/', methods=['POST', 'GET'])
# def uploadimage():
#     if request.method == "POST":
#         image = request.files['img']
#         temp_name = f"uploadimages/temp_{uuid.uuid4().hex}"
#         image.save(f'{temp_name}_{image.filename}')
#         print(f'{temp_name}_{image.filename}')
#         prediction = model_predict(f'./{temp_name}_{image.filename}')
#         return render_template(
#             'home.html',
#             result=True,
#             imagepath=f'/{temp_name}_{image.filename}',
#             prediction=prediction
#         )
#     else:
#         return redirect('/')

# if __name__ == "__main__":
#     app.run(debug=True)

# ---__--   -   -   -   -   -   -       --  -   -   -   -   -   -   -   -   -   -
from flask import Flask, render_template, request, redirect, send_from_directory, url_for, session
import numpy as np
import json
import uuid
import tensorflow as tf
import requests

app = Flask(__name__)
app.secret_key = 'agrivision_super_secret_key_change_me'

# FastAPI Authentication Backend URL
AUTH_API_BASE_URL = "http://127.0.0.1:8000/users"

# Load TensorFlow Model & Json Labels
model = tf.keras.models.load_model("models/Plant_disease_recog_model_pwp.keras")

with open("plant_disease.json", 'r') as file:
    plant_disease = json.load(file)

@app.route('/uploadimages/<path:filename>')
def uploaded_images(filename):
    return send_from_directory('./uploadimages', filename)

@app.route('/', methods=['GET'])
def home():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    return render_template('home.html')

@app.route('/about', methods=['GET'])
def about():
    return render_template('about.html')

@app.route('/profile', methods=['GET'])
def profile():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    
    user_email = session.get('user', 'user@example.com')
    user_name = session.get('user_name', user_email.split('@')[0].capitalize())
    test_count = session.get('test_count', 0)
    
    return render_template('profile.html', user_email=user_email, user_name=user_name, test_count=test_count)

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        try:
            response = requests.post(
                f"{AUTH_API_BASE_URL}/login",
                json={"email": email, "password": password},
                headers={"Content-Type": "application/json"}
            )

            if response.status_code == 200:
                res_data = response.json() if response.headers.get('content-type') == 'application/json' else {}
                
                session['user'] = email
                # Store user name or extract from email fallback
                session['user_name'] = res_data.get('name') if isinstance(res_data, dict) and res_data.get('name') else email.split('@')[0].capitalize()
                session['logged_in'] = True
                
                if 'test_count' not in session:
                    session['test_count'] = 0
                    
                return redirect(url_for('home'))
            else:
                error = "Invalid email or password. Please try again."
        except requests.exceptions.RequestException:
            error = "Authentication server is offline (http://127.0.0.1:8000)."

    return render_template('login.html', error=error)

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    error = None
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('password')

        try:
            response = requests.post(
                f"{AUTH_API_BASE_URL}/signup",
                json={
                    "name": name,
                    "email": email,
                    "password": password
                },
                headers={"Content-Type": "application/json"}
            )

            if response.status_code in (200, 201):
                session['user'] = email
                session['user_name'] = name if name else email.split('@')[0].capitalize()
                session['logged_in'] = True
                session['test_count'] = 0
                return redirect(url_for('home'))
            else:
                error = "Registration failed. User may already exist."
        except requests.exceptions.RequestException:
            error = "Authentication server is offline (http://127.0.0.1:8000)."

    return render_template('signup.html', error=error)

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

def extract_features(image):
    image = tf.keras.utils.load_img(image, target_size=(160, 160))
    feature = tf.keras.utils.img_to_array(image)
    feature = np.array([feature])
    return feature

def model_predict(image):
    img = extract_features(image)
    prediction = model.predict(img)
    prediction_label = plant_disease[prediction.argmax()]
    return prediction_label

@app.route('/upload/', methods=['POST', 'GET'])
def uploadimage():
    if not session.get('logged_in'):
        return redirect(url_for('login'))

    if request.method == "POST":
        image = request.files['img']
        temp_name = f"uploadimages/temp_{uuid.uuid4().hex}"
        image.save(f'{temp_name}_{image.filename}')
        prediction = model_predict(f'./{temp_name}_{image.filename}')
        
        # Increment prediction counter
        session['test_count'] = session.get('test_count', 0) + 1
        
        return render_template(
            'home.html',
            result=True,
            imagepath=f'/{temp_name}_{image.filename}',
            prediction=prediction
        )
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)