import requests
import time
import streamlit as st

def callapi(file,search,mod):
    start_time = time.time()  # Record start time
    url = "https://api.worqhat.com/api/ai/images/modify/v3/search-replace-image"
    payload = {
        "search_object" : [search],
        "modification": [mod] ,
        "output_type": "url"
        
         # Assuming 'prompt' is the modification field
    }
    files = {
        'existing_image': file  # Pass the file directly
    }
    headers = {
       
        'Accept': 'application/json',
        "Authorization": "Bearer sk-02e44d2ccb164c738a6c4a65dbf75e89"
    }
    st.write("The request is being sent")
    response = requests.request("POST",url, headers=headers, data=payload, files=files)
    end_time = time.time()  # Record end time
    duration = end_time - start_time  # Calculate duration
    if response.status_code == 200:
        return response.json()['image'], round(duration, 2)
    else:
        st.write("The request failed")
        return None, round(duration, 2)

st.title("Image Modifier")
st.write("Upload an image and modify it according to your needs.")

uploaded_image = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
prompt1 = st.text_input("Enter The object to search")
prompt2 = st.text_input("Enter the modification you want to do ")
if st.button("Send"):
    st.write("Generating the image ")
    response_v2, duration_v2 = callapi(uploaded_image,prompt1, prompt2)
    st.image(response_v2, caption=f"Modified image - Time taken: {duration_v2} seconds", use_column_width=True)
