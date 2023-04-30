import streamlit as st
import pandas as pd

st.title('title')
st.header('header')
st.subheader('subheader')
st.text('text')
st.markdown('## markdown')
code = '''st.title('title')
st.header('header')
st.subheader('subheader')
st.text('text')
st.markdown('## markdown')'''
st.code(code, language='python',line_numbers=True)
# colored text
st.success('성공적으로 저장하였습니다.')
st.warning('업로드할 수 없는 파일 형식입니다.')
st.info('알려드립니다.')
st.error('error')
st.exception('exception')

# super function
st.write('Normal')
st.write('## markdown text')
st.write(1+2)
st.write(dir(st))

# help info
st.help(range)

name = 'Kim Kibeom'

# pandas
st.title(' Data Display Elements')
st.header('Iris data display')
df = pd.read_csv("https://raw.githubusercontent.com/jmnote/zdata/master/R/iris.csv")
st.subheader('Method 1')
st.dataframe(df)
st.subheader('Method 2')
st.dataframe(df.style.highlight_max(axis=0))
st.table(df)
st.header('display json')
st.json({'data' : 'name'})
st.header('display code')
st.code('''
    print('hello streamlit')
''', language='python')

col1, col2, col3 = st.columns(3)
col1.metric('Temp', "70", "1.2")
col2.metric('Wind', '9 mph', '-8%')
col3.metric('Humidity', '86%', '4%')
if st.button('Submit', key=1):
    st.write(f'Name : {name}')
if st.button('Submit', key=2):
    st.write(f'Full Name : {name}')

st.header('Radio Button')
status = st.radio('What is your status',
                  ('Active', 'Inactive'))
if status == 'Active':
    st.success('You are active')
elif status == 'Inactive':
    st.warning('You are inactive')
st.header('Checkbox')
agree = st.checkbox('I agree')
if agree:
    st.write('You agreed')
my_lang = ['Python','C','C++','C#','Go',"Java"]
st.selectbox("Language", my_lang)
multi_choices = st.multiselect('Multi Select', my_lang)
