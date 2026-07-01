import streamlit as st
import requests
from bs4 import BeautifulSoup

# వెబ్‌సైట్ సెట్టింగ్స్
st.set_page_config(page_title="Web Scraper Bot", page_icon="🤖", layout="centered")

st.title("🤖 నా సొంత వెబ్ స్క్రాపర్ బాట్")
st.write("---")
st.markdown("### **ఇంటర్నెట్ నుండి ఆటోమేటిక్ గా డేటా లాగే రోబోట్!**")

st.write("నేను ఇప్పుడు 'quotes.toscrape.com' అనే వెబ్‌సైట్‌లోకి వెళ్లి అక్కడున్న డేటాని ఆటోమేటిక్ గా లాక్కొస్తాను. రెడీనా?")

# బటన్ నొక్కగానే రోబోట్ పని మొదలుపెడుతుంది
if st.button("🚀 ఇంటర్నెట్ నుండి కోట్స్ తీసుకురా", use_container_width=True):
    
    # 1. ఏ వెబ్‌సైట్‌కి వెళ్ళాలో ఆ లింక్ (URL) ఇస్తున్నాం
    url = "http://quotes.toscrape.com/"
    
    try:
        # 2. ఆ వెబ్‌సైట్‌కి రిక్వెస్ట్ పంపి, పేజీని డౌన్‌లోడ్ చేస్తున్నాం
        response = requests.get(url)
        
        # 3. ఆ పేజీలోని కోడ్ (HTML) ని BeautifulSoup తో చదువుతున్నాం
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # 4. అందులో 'text' అనే క్లాస్ ఉన్నవి కోట్స్, 'author' అనే క్లాస్ ఉన్నవి పేర్లు
        quotes = soup.find_all('span', class_='text')
        authors = soup.find_all('small', class_='author')
        
        st.success("✅ సక్సెస్! వెబ్‌సైట్ నుండి డేటా లాగడం పూర్తయింది. ఇవిగో టాప్ 5 కోట్స్:")
        st.write("---")
        
        # 5. లాక్కొచ్చిన డేటాలో మొదటి 5 వాటిని స్క్రీన్ మీద చూపిస్తున్నాం
        for i in range(5):
            st.info(f"💬 {quotes[i].text}")
            st.warning(f"✍️ - {authors[i].text}")
            
    except Exception as e:
        st.error("ఎక్కడో తేడా కొట్టింది బ్రో, ఆ వెబ్‌సైట్ మనల్ని బ్లాక్ చేసి ఉండొచ్చు!")