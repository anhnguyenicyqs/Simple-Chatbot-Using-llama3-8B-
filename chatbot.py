import requests
import json

def chat_with_llama(prompt):
    url = "http://localhost:11434/api/generate"
    data = {
        "model": "llama3",
        "prompt": prompt,
        "stream": False
    }
    response = requests.post(url, json=data)
    if response.status_code == 200:
        result = response.json()
        return result.get("response", "Không có phản hồi từ AI.")
    else:
        return "Lỗi khi kết nối với Ollama."

if __name__ == "__main__":
    print("Chatbot AI (Nhập 'exit' để thoát)")
    while True:
        user_input = input("Bạn: ")
        if user_input.lower() == "exit":
            break
        response = chat_with_llama(user_input)
        print("Chatbot:", response)
