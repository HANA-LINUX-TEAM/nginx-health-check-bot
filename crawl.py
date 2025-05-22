import os
import requests
from datetime import datetime
from bs4 import BeautifulSoup
try:
    res = requests.get(f"http://{os.environ['SERVER_IP']}/index.html", timeout=5)
    res.raise_for_status()
    html = res.text

    # ✅ HTML 파싱
    soup = BeautifulSoup(html, "html.parser")
    h1_text = soup.h1.get_text(strip=True) if soup.h1 else "❌ <h1> 태그 없음"

    # ✅ 디버깅용 출력
    print("응답 상태 코드:", res.status_code)
    print("HTML 길이:", len(html))
    print("<h1> 내용:", h1_text)

except Exception as e:
    h1_text = f"❌ 서버 응답 오류: {str(e)}"
    print("에러 발생:", h1_text)

payload = {
    "text": f"**🌐 nginx index.html의 내용**\n\n- 시간: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n```html\n{h1_text}\n```"
}

resp = requests.post(os.environ["WEBHOOK_URL"], json=payload)
print("Teams 응답 코드:", resp.status_code)
