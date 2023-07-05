import streamlit as st
import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader
from pathlib import Path

# USER AUTHENTICATION
with open(Path(__file__).parent / 'config.yml') as file:
    config = yaml.load(file, Loader=SafeLoader)

authenticator = stauth.Authenticate(
    config['credentials'],
    config['credentials']['cookie']['name'],
    config['credentials']['cookie']['key'],
    config['credentials']['cookie']['expiry_days'],
    config['credentials']['preauthorized']
)

name, authentication_status, username = authenticator.login('Login', 'main')

if 'authentication_status' not in st.session_state:
    st.session_state['authentication_status'] = False

if authentication_status:
    authenticator.logout('Logout', 'main')
    st.write(f'Welcome {name}')
    st.title('Some content')
elif authentication_status is False:
    st.error('Username/password is incorrect')
elif authentication_status is None:
    st.warning('Please enter your username and password')
