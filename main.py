import os
import requests
import google.generativeai as genai
from datetime import datetime

# 1. API 설정 (GitHub Secrets에서 불러옴)
genai.configure(api_key=os.environ["AIzaSyAGkaTuK1gNA5crWDCLuotAVVlcuVqVbB8"])
model = genai.GenerativeModel('gemini-1.5-flash')

class NexusEngine:
    def __init__(self):
        # 6개 국어 설정 (영, 중, 일, 서, 불, 한)
        self.langs = {
            "EN": "English", "CN": "Chinese", "JP": "Japanese", 
            "ES": "Spanish", "FR": "French", "KR": "Korean"
        }
        self.data_summary = ""

    def collect(self):
        print("데이터 수집 중...")
        # HuggingFace 트렌딩 데이터 샘플 수집
        try:
            res = requests.get("https://huggingface.co/api/trending?type=model").json()
            self.data_summary = f"Current Tech Trends: {res[:3]}"
        except:
            self.data_summary = "No new data found, analyzing general market trends."

    def generate(self):
        self.collect()
        for code, name in self.langs.items():
            print(f"{name} 리포트 생성 중...")
            prompt = f"""
            You are a $10M global tech strategist. 
            Analyze this data and write a high-value business report in {name}:
            {self.data_summary}
            Include: Business Opportunity, Technical Guide, and SEO Keywords.
            """
            response = model.generate_content(prompt)
            
            # 폴더 구조화 및 파일 저장
            path = f"content/{code.lower()}"
            os.makedirs(path, exist_ok=True)
            filename = f"{path}/{datetime.now().strftime('%Y-%m-%d')}.md"
            with open(filename, "w", encoding="utf-8") as f:
                f.write(response.text)
        print("모든 리포트 생성 완료!")

if __name__ == "__main__":
    NexusEngine().generate()
