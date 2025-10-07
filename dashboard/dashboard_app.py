import streamlit as st, json

st.title('Health Surveillance Dashboard')

with open('../backend/data.json','r') as f:
    data = json.load(f)

st.write('Collected Health Reports')
st.write(data)

st.write('Predicted Risk Alerts (Placeholder)')
st.write([{'village':'Example','risk':'Low'}])
