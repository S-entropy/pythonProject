import streamlit as st
import logging

LOGS_FORMAT = '%(levelname)s %(asctime)s.%(msecs)03d - %(message)s'

logging.basicConfig(level=logging.DEBUG, format=LOGS_FORMAT)
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter(LOGS_FORMAT)

file_handler = logging.FileHandler('activity.log')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

st.title('Adding Logs To App')
st.text('Track All Activities/Pages Visited For App')

menu = ['Home', 'EDA', 'ML', 'About']
choice = st.sidebar.selectbox('Menu', menu)

if choice == 'Home':
    st.subheader('Home Section')
    logger.info('Home Section')

elif choice == 'EDA':
    st.subheader('EDA Section')
    logger.info('EDA Section')

elif choice == 'ML':
    st.subheader('ML Section')
    logger.info('ML Section')

elif choice == 'Analysis':
    st.subheader('Analysis')
    logger.info('Analysis Section')

else:
    st.subheader('About')
    logger.info('About Section')