def soultion(s):
    ## 대문자, 소문자 구별 x
    s = s.lower()
    s = list(s)

    ## http
    http = list()

    ## https
    https = list()

    ## 문자열 순회
    idx = 0
    while idx < len(s):
        if idx + 7 < len(s) and "".join(s[idx : idx + 7]) == "http://":
            ## http로 시작하는 url
            url = ""
            idx += 7
            is_alph = True
            while idx < len(s) and s[idx] != ".":
                url += s[idx]
                if not (0<= ord(s[idx]) - ord('a') <= 25):
                    is_alph = False
                idx += 1
            
            if idx + 1 < len(s):
                idx += 1
        
            if idx + 3 <= len(s) and "".join(s[idx : idx + 3]) in ("org", "net", "com"):
                com_url = url + "." + "".join(s[idx : idx + 3])
                if com_url not in http and len(url) >= 3 and is_alph:
                    http.append(com_url)
                idx += 3
            elif idx + 5 <= len(s) and "".join(s[idx : idx + 5]) == "co.kr":
                com_url = url + "." + "".join(s[idx : idx + 5])
                if com_url not in http and len(url) >= 3 and is_alph:
                    http.append(com_url)
                idx += 5
        elif idx + 8 < len(s) and "".join(s[idx: idx + 8]) == "https://":
            ## https로 시작하는 url
            url = ""
            idx += 8
            is_alph = True
            while idx < len(s) and s[idx] != ".":
                url += s[idx]
                if not (0 <= ord(s[idx]) - ord('a') <= 25):
                    is_alph = False
                idx += 1
            
            if idx + 1 < len(s):
                idx += 1
            
            if idx + 3 <= len(s) and "".join(s[idx : idx + 3]) in ("org", "net", "com"):
                com_url = url + "." + "".join(s[idx : idx + 3])
                if com_url not in https and len(url) >= 3 and is_alph:
                    https.append(com_url)
                idx += 3
            elif idx + 5 <= len(s) and "".join(s[idx : idx + 5]) == "co.kr":
                com_url = url + "." + "".join(s[idx : idx + 5])
                if com_url not in https and len(url) >= 3 and is_alph:
                    https.append(com_url)
                idx += 5
        else:
            idx += 1

    print("http:", http)
    print("https:", https)

    answer = len(http) + len(https)
    return answer 

## 문제: 문자열에서 url 파싱
### 1. 소문자/대문자 구별 없음
### 2. url은 http://, https://로 시작
### 3. url은 com, org, net, co.kr로 끝남
### 4. http와 com등의 끝 문자사이 문자는 3글자 이상 ex) http://naver.com은 naver(5글자)
### 5. http와 com등의 끝 문자사이 문자는 알파벳만

print("---------------------------------------------------------------------------------------------------")

s = "http://123yd.co.krhttps://colab.com/drive/12k3jYYhttp://colab.comTQsK5URhttp://ccc.co.krVxeJspSsBS1RmHfsug#scrollTo=l0gphJzsRDV7https://younhwan.com/younhwan97/bf98b53173ce464481c235a4e5d3535ahttp://navefr.com"
print("# case 1")
print(soultion(s))
print("---------------------------------------------------------------------------------------------------")

s = "123123"
print("# case 2")
print(soultion(s))
print("---------------------------------------------------------------------------------------------------")

s = "ccc.co.kr"
print("# case 3")
print(soultion(s))
print("---------------------------------------------------------------------------------------------------")

s = "http://http://naver.com"
print("# case 4")
print(soultion(s))
print("---------------------------------------------------------------------------------------------------")
