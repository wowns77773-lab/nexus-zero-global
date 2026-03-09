import os
import google.generativeai as genai

# 1. API 키 확인 (연료 체크)
api_key = os.environ.get("AIzaSyAGkaTuK1gNA5crWDCLuotAVVlcuVqVbB8")

if not api_key:
    print("❌ 에러: API 키가 설정되지 않았습니다! Settings > Secrets를 확인하세요.")
    exit(1)

try:
    # 2. AI 엔진 설정
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-1.5-flash')

    # 3. 테스트 실행
    response = model.generate_content("Hello, say 'Success!' in Korean.")
    print(f"✅ AI 응답 성공: {response.text}")

    # 4. 결과 저장용 폴더 만들기
    os.makedirs("content", exist_ok=True)
    with open("content/test.txt", "w", encoding="utf-8") as f:
        f.write(f"AI가 생성한 메시지: {response.text}")

except Exception as e:
    print(f"❌ 실행 중 에러 발생: {e}")
    exit(1)
