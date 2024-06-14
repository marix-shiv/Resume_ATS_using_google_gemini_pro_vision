#1. Feild to put my job description
#2. Upload the pdf
#3. PDF to image ---> Processing ---> Google gemini pro models
#4. Prompt template[Multiple Prompts]
from dotenv import load_dotenv

load_dotenv()

import streamlit as st
import os
from PIL import Image
import pdf2image
import google.generativeai as genai
import io
import base64
genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))

def get_gemini_response(input,pdf_content,prompt):
    model= genai.GenerativeModel('gemini-pro-vision')
    response = model.generate_content([input,pdf_content[0],prompt])
    return response.text

def input_pdf_setup(uploaded_file):
    if uploaded_file is not None:
        # convert the pdf to image
        images = pdf2image.convert_from_bytes(uploaded_file.read())
        first_page = images[0]

        #convert into bytes
        img_byte_arr = io.BytesIO()
        first_page.save(img_byte_arr, format='JPEG')
        img_byte_arr = img_byte_arr.getvalue()

        pdf_parts = [
            {
                "mime_type": "image/jpeg",
                "data": base64.b64encode(img_byte_arr).decode()
            }
        ]
        return pdf_parts
    else:
        raise FileNotFoundError("No file Found")

## Streamlit App
st.set_page_config(page_title="ATS Resume Expert")
st.header("ATS Tracking System")
input_text = st.text_area("Job Description: ",key="input")
uploaded_file = st.file_uploader("Upload your resume in pdf format",type=["pdf"])
if uploaded_file is not None:
    st.write("PDF Uploaded Successfully")

    submit1 = st.button("Tell me about the Resume")
    # submit2 = st.button("How can i Improvise my Skills")
    submit2 = st.button("Percentage Match")

    input_prompt1 = """
    You are an experineced HR with tech expertise in the feild of 
    Data Science, Full Stack web development,Big data Engineering, DevOps, Data Analyst, Your task is to review the provided
    resume against the job description for these profiles.
    Please share your professional evaluation on weather the candidate's profile aligns
    with the role. HIghlight the strengeths and weaaknesses of the applicant in the relation to the 
    specified job requirement.
    """

    input_prompt2 = """
    you are skilled ATS (Applicant Tracking System) scanner with a deep understanding of Data Science, Full Stack web development,Big data Engineering, DevOps, Data Analyst 
    and deep ATS functionality, your task is to evaluate the resume against the provided job description
    give me the percentage of match if the resume matches job description. First output should come as percentage 
    and then keywords missing and last final thoughts.
    """

    if submit1:
        if uploaded_file is not None:
            pdf_content = input_pdf_setup(uploaded_file)
            response = get_gemini_response(input_prompt1,pdf_content,input_text)
            st.subheader("The response is: ")
            st.write(response)
        else:
            st.write("Please upload a resume")
    elif submit2:
        if uploaded_file is not None:
            pdf_content = input_pdf_setup(uploaded_file)
            response = get_gemini_response(input_prompt2,pdf_content,input_text)
            st.subheader("The response is: ")
            st.write(response)
        else:
            st.write("Please upload a resume")