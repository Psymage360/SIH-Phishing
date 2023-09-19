import numpy as np
import pandas as pd
# from sklearn.preprocessing import StandardScaler
# from src.pipeline.classify_pipeline import CustomData,ClassifyPipeline    
from flask import Flask, render_template, request, redirect, url_for, flash
import pickle
import secrets

secret_key = secrets.token_hex(16)
application=Flask(__name__)
application.secret_key=secret_key
app=application
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        choice = request.form.get('choice')
        if choice == 'url':
            return redirect(url_for('enter_url'))
        elif choice == 'image':
            return redirect(url_for('upload_image'))
    return render_template('index.html')
@app.route('/enter_url', methods=['GET', 'POST'])
def enter_url():
    if request.method=='GET':
        return render_template('enter_url.html')
    elif request.method == 'POST':
        url = request.form.get('url')
        model_path='artifacts/url_pickle.pkl'
        loaded_model=pickle.load(open(model_path,'rb'))
        check=[]
        check.append(url)
        results=loaded_model.predict(check)
        print(results)
        # flash('URL submitted for processing.')
        return render_template('index.html',results=results[0])
@app.route('/upload_image', methods=['GET', 'POST'])
def upload_image():
    if request.method == 'POST':
        file = request.files['file']
        if file:
            # Handle image upload here
            # Send the uploaded image to your ML app for processing
            flash('Image uploaded and submitted for processing.')
    return render_template('upload_image.html')
if __name__=="__main__":
    app.run(host="0.0.0.0",debug=True)
