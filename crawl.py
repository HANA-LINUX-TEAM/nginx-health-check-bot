import os
import requests
from datetime import datetime

try:
    res = requests.get(f"http://{os.environ['SERVER_IP']}/index.html", timeout=5)
    res.raise_for_status()
    html = res.text
    snippet = html[:1000]
    if len(html) > 1000:
        snippet += "\n... (이하 생략)"

    # ✅ 디버깅용 출력
    print("응답 상태 코드:", res.status_code)
    print("HTML 길이:", len(html))
    print("HTML 미리보기:\n", snippet[:300])

except Exception as e:
    snippet = f"❌ 서버 응답 오류: {str(e)}"
    print("에러 발생:", snippet)

payload = {
    "text": f"**🌐 nginx index.html 전체 HTML 소스**\n\n- 시간: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n```html\n{snippet}\n```"
}

resp = requests.post(os.environ["WEBHOOK_URL"], json=payload)
print("Teams 응답 코드:", resp.status_code)
