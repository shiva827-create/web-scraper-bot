
       import streamlit as st
import requests
from bs4 import BeautifulSoup

st.set_page_config(page_title="Amazon Tracker", page_icon="🛒", layout="centered")

st.title("🛒 అమెజాన్ ప్రైస్ & డేటా స్క్రాపర్")
st.write("---")
st.write("అమెజాన్ సెక్యూరిటీని దాటి డేటాని లాగే స్టీల్త్ (Stealth) రోబోట్!")

# యూజర్ దగ్గర నుండి అమెజాన్ లింక్ తీసుకోవడం
product_url = st.text_input("🔗 ఏదైనా అమెజాన్ ప్రోడక్ట్ లింక్ ఇక్కడ పేస్ట్ చేయండి:")

if st.button("🚀 డేటా లాక్కురా!", use_container_width=True):
    if product_url:
        # దొంగ వేషం: రోబోట్ లాగా కాకుండా, క్రోమ్ బ్రౌజర్ లాగా వెళ్ళడానికి ఈ హెడర్స్ వాడతాం
        HEADERS = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
            'Accept-Language': 'en-US, en;q=0.5'
        }
        
        try:
            with st.spinner("అమెజాన్ సెక్యూరిటీని దాటుకుంటూ వెళ్తున్నా... 🕵️‍♂️"):
                # వెబ్‌సైట్‌కి వెళ్లడం
                response = requests.get(product_url, headers=HEADERS)
                soup = BeautifulSoup(response.content, 'html.parser')
                
                # ప్రోడక్ట్ పేరు (Title) లాగడం
                title_element = soup.find("span", attrs={"id": 'productTitle'})
                
                if title_element:
                    title = title_element.text.strip()
                    st.success("✅ సక్సెస్! అమెజాన్ సెక్యూరిటీని క్రాక్ చేశాం!")
                    st.info(f"📦 **ప్రోడక్ట్ పేరు:** {title}")
                else:
                    st.warning("⚠️ అరెరె! అమెజాన్ మన రోబోట్‌ని పసిగట్టేసింది. CAPTCHA (బొమ్మల పజిల్) అడుగుతోంది!")
                    
        except Exception as e:
            st.error("ఓప్స్! లింక్ తప్పుగా ఉందో, లేక సర్వర్ క్రాష్ అయ్యిందో చెక్ చెయ్ బ్రో.")
    else:
        st.error("ముందు పైన ఏదైనా అమెజాన్ లింక్ పేస్ట్ చెయ్ తమ్ముడూ!")
