import streamlit as st

st.title('Software Developer Salary Prediction')
st.write("""

> This Machine Predict Salary of a Software Engineer Using Various Predictors like,**Experience** and **Education**
 

""")

st.subheader('Explore or Predict')

prediction = st.markdown("""
- **Model Prediction** [Predict]( http://localhost:8501/Prediction)
- **Model Explore** [Explore]( http://localhost:8501/EDA)
""")




