import streamlit as st

st.set_page_config(
    page_title="Demo-Interface v0.0",
    layout='wide'
)

st.write("Demo Interface v0.0")

#def check_desc():
    #parse input to llm and return feedback

create,results=st.tabs(['Create post','View results'])

with create:
    job_title=st.text_input("Enter job title")
    job_description=st.text_input("Enter job description")
    review=st.button("Click here for AI review")
    normal,enhanced=st.columns([1,2])
    with normal:
        st.write("Proceed with your input \n"+job_description)
        status1=st.button("Post to linkedin")
    with enhanced:
        st.write("Enhanced Description: \n"+job_description)
        status2=st.button("Post Enhanced description to linkedin")
