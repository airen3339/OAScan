import httpx
from lib.get_normal_url import get_standard_url
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36",
    "Content-Type": "application/x-www-form-urlencoded",
}

def poc(target):
    try:
        target = get_standard_url(target)
        url = target + '/seeyon/wpsAssistServlet'
        req = httpx.get(url, headers=headers)
        if "flag is empty" in req.text and req.status_code == 200:
            print("\033[0;31m 致远OA v8文件上传漏洞：" + url)
    except:
        pass


