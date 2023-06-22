'''
    1. 인가코드 받기
    https://kauth.kakao.com/oauth/authorize
    
    - client_id         : REST API KEY
    - redirect_uri      : https://localhost.com
    - response_type     : code


    응답결과 : code (인가코드)
'''
a = '636004344b306ca0cc7283d41ffc4f1b'
b = 'https://localhost.com'
c = 'code'

req_url = 'https://kauth.kakao.com/oauth/authorize?client_id={}&redirect_uri={}&response_type={}'.format(a,b,c)
print(req_url)


# 인가코드 요청 URL
# https://kauth.kakao.com/oauth/authorize?client_id=636004344b306ca0cc7283d41ffc4f1b&redirect_uri=https://localhost.com&response_type=code


# 인가코드
auth_code = '3B2OR05aHHVdLkGkH31VyEbPtMWJY_XICJWQV5NXPwzBBNJjYZLI4hCoknyRYMVhhmEYPAopyNoAAAGI4fz7Zg'

# 액세스 토큰 받기
url = 'https://kauth.kakao.com/oauth/token'

# 요청 정보
data = {
    'grant_type'    : 'authorization_code',
    'client_id'     : a,                    # REST API KEY
    'redirect_uri'  : b,    
    'code'          : auth_code             # 인가코드
}

import requests

# POST 방식으로 URL 요청
response = requests.post(url, data=data)


# 요청 실패
if response.status_code != 200:
    print('요청 실패!', response.json())
# 요청 성공
else:
    result = response.json()
    token = result['access_token']
    print(result)
    print(token)

# access_token
# 2U9e1tZAKSRe3ZtNa_x64bNccYRtGVoL6YWszISTCj1z7AAAAYjh_qUD