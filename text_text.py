import google.generativeai as genai

api_key = 'AIzaSyBc8qhYVRffNlIgL6wbIGmvFN0xBune5yk'
genai.configure(api_key = api_key) #辨識apikey

model = genai.GenerativeModel('gemini-pro') #選擇要使用的模型
chat = model.start_chat(history=[]) #開始對話
response=chat.send_message("要說的內容") #輸入內容
print(response.text) #取得並輸出回覆
