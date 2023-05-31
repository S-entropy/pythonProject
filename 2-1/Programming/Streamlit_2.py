import streamlit as st
import pandas as pd
age = st.slider('How old are you?', 1, 120, 18)
st.write("I'm", age, 'yeaes old')

values = st.slider('Select a range of values', 0.0, 100.0, (25.0, 75.0))
st.write('Values:', values)

from datetime import time
appointment = st.slider('Schedule your appointment:',
                        value=(time(11,30), time(12,45)))
st.write("Schedule:", appointment)
from datetime import datetime
start_time = st.slider("When do you start?", value=datetime(2020, 1, 1, 9, 30),
                       format="MM/DD/YY - hh:mm")
color = st.select_slider('Select a color of the rainbow',
                         options = ['red', 'blue', 'orange'])
st.write('My favorite color is', color)

title = st.text_input('Movie title', 'Life of Brian')
st.write('The current movie title is {}'.format(title))

first_name = st.text_input('Enter your first name', max_chars=10)
st.write('Your first name is {}'.format(first_name))
number = st.number_input('Insert a number')
st.write('The current number is', number)

import datetime

d = st.date_input("When's your birthday", datetime.date(2019,7,6))
st.write('Your birthday is:', d)

t = st.time_input('Set an alarm for', datetime.time(8, 45))
st.write('Alarm is set for', t)