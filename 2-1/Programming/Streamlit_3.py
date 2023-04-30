import streamlit as st
import pandas as pd
from PIL import Image
import docx2txt as docx2txt
from PyPDF2 import PdfFileReader
import os
@st.cache
def load_image(img_file):
    return Image.open(img_file)

def read_pdf(file):
    pdf = PdfFileReader(file)
    count = pdf.numPages
    all_page_text = ''
    for i in range(count):
        page = pdf.getPage(i)
        all_page_text += page.extractText()
    return all_page_text

def save_upload_file(uploaded_file):
    with open(os.path.join('tmp', uploaded_file), 'wb') as f:
        f.write()
    return st.success('Saved file : {} in tmp'.format(uploaded_file.name))

st.title(' Upload')
menu = ['Home', 'Dataset', 'DocumentFiles', 'About']
choice = st.sidebar.selectbox('Menu', menu)

if choice == 'Home':
    st.subheader('Home')
    img_file = st.file_uploader('Upload images', type=['png','jpg','jpeg'])

    if img_file is not None:
        st.write(type(img_file))
        img_details = {'filename': img_file.name,
                       'filetype': img_file.type,
                       'filesize': img_file.size}
        st.write(img_details)
        st.image(load_image(img_file))
elif choice == 'Dataset':
    st.subheader('Dataset')
    data_file = st.file_uploader('Upload CSV', type=['csv'])
    if data_file is not None:
        st.wwite(type(data_file))

        file_details = {'filename': data_file.name,
                       'filetype': data_file.type,
                       'filesize': data_file.size}
        st.write(file_details)

        df = pd.read_csv(data_file)
        st.dataframe(df.descrbe())
elif choice == 'DocumentFiles':
    st.subheader('DocumentFiles')
    docs_file = st.file_uploader('Upload Document', type=['pdf', 'docs', 'txt'])

    if st.button('Process'):
        if docs_file is not None:
            file_details = {'filename': docs_file.name,
                       'filetype': docs_file.type,
                       'filesize': docs_file.size}
            st.write(file_details)
            if docs_file.tyype == 'text/plain':
                raw_text = str(docs_file.read(), 'utf-8')
                st.write(raw_text)
            elif docs_file.type == 'applicaton/pdf':
                raw_text = read_pdf(docs_file)
                st.write(raw_text)
            else:
                raw_text = docx2txt.process(docs_file)
                st.write(raw_text)
