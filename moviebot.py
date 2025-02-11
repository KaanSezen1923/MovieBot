import os 
import requests
import streamlit as st 
from dotenv import load_dotenv

load_dotenv()

app_token=os.getenv("APPLICATION_TOKEN")


BASE_API_URL = "https://api.langflow.astra.datastax.com"
LANGFLOW_ID = "56c73e09-63cc-4139-b029-5382c8918c3a"
FLOW_ID = "d2829bbe-15bb-4d04-86f2-3ab19d7daf8a"
APPLICATION_TOKEN = app_token
ENDPOINT = "moviebot" 


def run_flow(message: str) -> dict:
    api_url = f"{BASE_API_URL}/lf/{LANGFLOW_ID}/api/v1/run/{ENDPOINT}"

    payload = {
        "input_value": message,
        "output_type": "chat",
        "input_type": "chat",
    }

    headers = {"Authorization": "Bearer " + APPLICATION_TOKEN, "Content-Type": "application/json"}
    response = requests.post(api_url, json=payload, headers=headers)
    return response.json()


st.title("MovieBot")
    
if "messages" not in st.session_state:
        st.session_state["messages"] = []
        
for message in st.session_state["messages"]:
        with st.chat_message(message["role"]):
            st.write(message["content"])
    

    
if user_query := st.chat_input("Ne izlemek istersiniz?"):
        with st.chat_message("user"):
            st.write(user_query)
        st.session_state["messages"].append({"role": "user", "content": user_query})
        
            
    
        try:
            with st.spinner("Running flow..."):
                response = run_flow(user_query)
            response = response["outputs"][0]["outputs"][0]["results"]["message"]["text"]
            with st.chat_message("assistant"):
                st.write(response)
            st.session_state["messages"].append({"role": "assistant", "content": response})
        except Exception as e:
            st.error(str(e))

