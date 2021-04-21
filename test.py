from passlib.hash import sha256_crypt

password = sha256_crypt.encrypt("password")    #encrypt 바꿔준다는 의미

print(password)

print(sha256_crypt.verify("password", password))  #비밀번호가 뭔지 모르지만 검증해주는것 맞으면 True 틀리면 False