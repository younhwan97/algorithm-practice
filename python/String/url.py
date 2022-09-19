def soultion(s):
    ## 대문자, 소문자 구별이 없다.
    s = s.lower()
    s = list(s)

    ## http
    http = list()

    ## https
    https = list()

    idx = 0
    while idx < len(s):
        if idx + 7 < len(s) and "".join(s[idx: idx + 7]) == "http://":
            ## http로 시작하는 url
            url = ""
            idx += 7
            is_alph = True

            while s[idx] != ".":
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
            elif idx + 5 <= len(s) and "".join(s[idx : idx + 5]) in ("co.kr"):
                com_url = url + "." + "".join(s[idx : idx + 5])
                if com_url not in http and len(url) >= 3 and is_alph:
                    http.append(com_url)
                idx += 5
        elif idx + 8 < len(s) and "".join(s[idx: idx + 8]) == "https://":
            ## https로 시작하는 url
            url = ""
            idx += 8
            is_alph = True

            while s[idx] != ".":
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
            elif idx + 5 <= len(s) and "".join(s[idx : idx + 5]) in ("co.kr"):
                com_url = url + "." + "".join(s[idx : idx + 5])
                if com_url not in https and len(url) >= 5 and is_alph:
                    https.append(com_url)
                idx += 5
        else:
            idx += 1

    print(http)
    print(https)

    answer = len(http) + len(https)
    return answer 

s = "http://aasdas.co.kr"
print(soultion(s))