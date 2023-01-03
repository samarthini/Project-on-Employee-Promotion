# -*- coding: utf-8 -*-
"""
Created on Tue Sep 20 12:32:27 2022

@author: DELL
"""

import numpy as np
import pickle
import streamlit as st

#Loading the saved model
loaded_model = pickle.load(open('gbc_model_pickle', 'rb'))

# creating a function for Prediction

from PIL import Image
image = Image.open("promotion.jpg")
st.image(image)

def Employee_Promotion_prediction(input_data):
    

    # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)

    if (prediction[0] == 0):
      return "Promoted"
    else:
      return "Not Promoted"
  
    
def main():
      # giving a title
 
    html_temp="""
    <div style ="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Employee_Promotion_prediction app 
    
    """
    
    st.markdown(html_temp,unsafe_allow_html=True) 
    
    # getting the input data from the user
    	
    
    no_of_trainings = st.text_input('no_of_trainings')
    previous_year_rating = st.text_input(' previous_year_rating')
    length_of_service = st.text_input('length_of_service')
    awards_won = st.text_input('awards_won')
    avg_training_score = st.text_input('avg_training_score')
    
    # code for Prediction
    Promoted = ''
    
    # creating a button for Prediction
    
    if st.button('Predict'):
        Promoted = Employee_Promotion_prediction([no_of_trainings,previous_year_rating,length_of_service,awards_won,avg_training_score])        
    st.success(Promoted)
    
if __name__ == '__main__':
    main()
