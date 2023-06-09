import streamlit as st
import datetime
from todo_firebase import DB, Auth
import pandas as pd
# DB 객체 생성
db = DB()
# DB 연결
DB.connect_db()
# streamlit 설정: layout="wide" -> 넓은 화면 사용
st.set_page_config(layout="centered")

# 사이드 바 생성
sb = st.sidebar

if Auth.authenticate_token(Auth.load_token()):
    st.session_state['login'] = True
else:
    st.session_state['login'] = False

# 사이드바에 선택상자를 메뉴로 사용
options = []
if st.session_state.login == True:
    options.append('할일')
    options.append('로그아웃')

else:
    options.append('로그인')
    options.append('사용자 등록')
    options.append('비밀번호 초기화')

menu = sb.selectbox('메뉴', options, key='menu_key')

if menu == '할일' and st.session_state.login == True:

    st.subheader('할일입력')

    # 할일 입력 폼
    # 내용, 날짜, 추가 버튼
    todo_content = st.text_input('할 일', placeholder='할 일을 입력하세요.')
    col1, col2, col3 = st.columns([2,2,2])
    todo_date = col1.date_input('날짜')
    todo_time = col2.time_input('시간')
    completed = st.checkbox('완료')
    btn = st.button('추가')
    if btn:


        db.insert_todo(
            {
                'todo_content': todo_content,
                'todo_date': todo_date.strftime('%Y-%m-%d'),
                'todo_time': todo_time.strftime('%H:%M'),
                'completed': completed,
                'reg_date': datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            })

        st.experimental_rerun()

    st.subheader('할일목록')


    def change_state(*args, **kargs):
        db.update_task_state(args[0], {'completed': st.session_state['completed'+args[0]]})

    def change_content(*args, **kargs):
        print(args[0], args[1])
        db.update_task_state(args[0], {'todo_content': st.session_state['todo_content' + args[0]]})

    def change_date(*args, **kargs):
        db.update_task_state(args[0], {'todo_date': st.session_state['todo_date'+args[0]].strftime('%Y-%m-%d')})

    def change_time(*args, **kargs):
        db.update_task_state(args[0], {'todo_time': st.session_state['todo_time'+args[0]].strftime('%H:%M')})

    def delete_todo(*args, **kargs):
        db.delete_todo(args[0])

    todos = db.read_todos()
    todos = list(todos.values())
    for todo in todos:
        todo['todo_date']=datetime.datetime.strptime(todo['todo_date'], '%Y-%m-%d')
        todo['todo_time']=datetime.datetime.strptime(todo['todo_time'], '%H:%M')
        todo['reg_date']=datetime.datetime.strptime(todo['reg_date'],'%Y-%m-%d %H:%M:%S')
    keyv='0'
    todos2 = pd.DataFrame(todos)
    if todos2 is not None:
        lasttodos = st.data_editor(
            todos2,
            column_order=('completed', 'todo_content', 'todo_date', 'todo_date', 'reg_date'),
            column_config={
                'completed': st.column_config.CheckboxColumn("완료여부"),
                'todo_content': st.column_config.TextColumn("할일"),
                'todo_date': st.column_config.DateColumn("날짜"),
                'todo_time': st.column_config.TimeColumn("시간"),
                'reg_date': st.column_config.DatetimeColumn('등록일시')
            }
            , hide_index=True
            , key=keyv
        )
    l = list(str(lasttodos).split('\n'))
    copyl = []
    for i in l:
        copyl.append(list(i.split()))
    print(copyl)
    cnt=0
    for lis in copyl:
        if cnt==0:
            cnt+=1
            continue
        st.json({
            "todo_content": lis[1][0]=='T',
            "todo_date": lis[2],
            "todo_time": lis[3],
            "completed": lis[4],
            "reg_date": lis[5]
        })
elif menu == '로그인':

    st.subheader('로그인')
    with st.form(key='login_form'):

        user_email = st.text_input('이메일')
        user_pw = st.text_input('비밀번호', type='password')

        btn_login = st.form_submit_button('로그인')

        if btn_login:
            idToken = Auth.login_user(user_email, user_pw)
            if idToken is not None:
                Auth.store_session(idToken)
                st.session_state['login'] = True
                menu = '할일'
                st.experimental_rerun()
            else:
                st.error('아이디, 비밀번호를 확인 후 다시 로그인하세요.')


elif menu == '사용자 등록':

    st.subheader('사용자 등록')
    with st.form(key='user_reg_form'):

        user_name = st.text_input('이름')
        user_email = st.text_input('이메일')
        user_pw = st.text_input('비밀번호', type='password')

        btn_user_reg = st.form_submit_button('사용자 등록')

        if btn_user_reg:
            res = None
            res = Auth.create_user(user_name, user_email, user_pw)
            if res is None:
                st.info('사용자가 등록되었습니다.')
            else:
                st.error(res)

elif menu == '로그아웃':

    st.info('로그아웃 하려면 로그아웃 버튼을 클릭하세요.')
    btn_logout = st.button('로그아웃')
    if btn_logout:
        Auth.revoke_token(Auth.load_token())
        st.experimental_rerun()

elif menu == '비밀번호 초기화':

    st.subheader('비밀번호 초기화')

    with st.form(key='pw_reset_form'):

        user_email = st.text_input('이메일')

        btn_reset = st.form_submit_button('비밀번호 초기화 메일 발송')

        if btn_reset:

            if Auth.reset_password(user_email):
                st.info('이메일을 확인하세요.')
            else:
                st.error('이메일이 정확한지 확인하세요!')