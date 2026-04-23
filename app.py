import streamlit as st
import joblib
import numpy as np

model = joblib.load("mental_health_model.pkl")

st.title("Teen Mental Health Predictor")

age = st.number_input("Age",13,19)

gender = st.selectbox(
"Gender",
["Female","Male"]
)

gender = 0 if gender=="Female" else 1

social_media = st.slider(
"Daily Social Media Hours",
1.0,8.0
)

platform = st.selectbox(
"Platform Usage",
["Instagram","TikTok","Both"]
)

platform_map = {
"Instagram":0,
"TikTok":1,
"Both":2
}

platform = platform_map[platform]

sleep = st.slider("Sleep Hours",4.0,9.0)

screen = st.slider(
"Screen Time Before Sleep",
0.5,3.0
)

academic = st.slider(
"Academic Performance",
1.0,10.0
)

physical = st.slider(
"Physical Activity",
1.0,10.0
)

social = st.selectbox(
"Social Interaction",
["Low","Medium","High"]
)

social_map={
"Low":0,
"Medium":1,
"High":2
}

social=social_map[social]

stress=st.slider("Stress Level",1,10)
anxiety=st.slider("Anxiety Level",1,10)
addiction=st.slider("Addiction Level",1,10)

screen_exposure=sleep+screen

features=np.array([[age,gender,social_media,
platform,sleep,screen,
academic,physical,social,
stress,anxiety,addiction,
screen_exposure]])

if st.button("Predict"):

    prediction=model.predict(features)

    if prediction[0]==1:
        st.error("High Depression Risk")
    else:
        st.success("Low Depression Risk")