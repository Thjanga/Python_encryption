# 알파벳 암호화
alphabet_E = {'a':'01',
            'b':'02',
            'c':'03',
            'd':'04',
            'e':'05',
            'f':'06',
            'g':'07',
            'h':'08',
            'i':'09',
            'j':'10',
            'k':'11',
            'l':'12',
            'm':'13',
            'n':'14',
            'o':'15',
            'p':'16',
            'q':'17',
            'r':'18',
            's':'19',
            't':'20',
            'u':'21',
            'v':'22',
            'w':'23',
            'x':'24',
            'y':'25',
            'z':'26',
            ' ':'32'}

# 알파벳 복호화 (alpha_E의 key,value 바꾸기)
alphabet_D = {n: c for c,n in alphabet_E.items()}

# 유클리드 호제법을 이용한 최대공약수 구하기
def gcd(a,b):
    if(b==0):
        return abs(a)
    else:
        return gcd(b,a%b)
    
# 암호화 (e, d, 공개키 구하기)
def rsa(p,q):
    # 공개키 부분
    N = p*q

    # 개인키 부분
    N0 = (p-1) * (q-1)

    # e 구하기 (공개키)
    for i in range(2,N0):
        if(gcd(i,N0)==1):
            e = i
            break

    # d 구하기 (개인키)
    for i in range(2,N0):
        if((e*i)%N0==1):
            d = i
            break
    
    return N,e,d

# 문자 암호화
def encrypt(char):
    return str((int(char)**e)%N).zfill(2)

# 문자 복호화
def decrypt(char):
    return str((int(char)**d)%N).zfill(2)

# 문자열 나누기
def split(word):
    return [char for char in word]

# 메시지 암호화
def encrypt_msg(msg):

    # 소문자로 변경
    plaintext = msg.lower().split()
    encrypted = []

    for word in plaintext:
        
        chars = split(word)

        encrypted_chars = [encrypt(alphabet_E[char]) for char in chars]

        encrypted_word = ' '.join(encrypted_chars)
        encrypted.append(encrypted_word)

    encrypted = f' {encrypt(alphabet_E[' '])} '.join(encrypted)

    return encrypted

# 메시지 복호화
def decrypt_msg(msg):

    encryptd = msg.split()
    decrypted = []
    plaintext = []

    for char in encryptd:
        decrypted.append(decrypt(char))

    for char in decrypted:
        plaintext.append(alphabet_D[char])

    plaintext = ''.join(plaintext)

    return plaintext

def option():
    print(" 0 - 키 보여주기\n","1 - 파일 암호화\n","2 - 파일 복호화\n","3 - 터미널 암호화\n","4 - 터미널 복호화\n","5 - 종료")

def check_prime(p):
    for i in range(2,p):
        if(p%i==0):
            return 1
        i*=i
    return 0

# 소수 입력받기
while 1:
    p = int(input("첫번째 소수: "))
    check_prime(p)
    if (check_prime(p)==1):
        print("소수가 아닙니다.")
        continue
    q = int(input("두번째 소수: "))
    check_prime(q)
    if (check_prime(q)==1):
        print("소수가 아닙니다.")
        continue
    if (check_prime(p)==0 and check_prime(q)==0):
        break

print()

N,e,d = rsa(p,q)

def showkey():
    print(f"공개키: E: {e} N: {N}\n")
    print(f"개인키: D: {d} N: {N}\n")

while 1:

    option()    
    print("옵션을 선택하세요\n")

    selection = input()
    if(selection == '0'):
        showkey()

    elif(selection == '1'):
        with open("input.txt",'r') as fin:
            msg = fin.read()
            
        with open("encrypted.txt",'w') as fout:
            fout.write(encrypt_msg(msg))

        print("파일 암호화 성공\n")

        encrypt_msg(msg)
    elif(selection == '2'):

        with open("encrypted.txt",'r') as fin:
            msg = fin.read()
            
        with open("decrypted.txt",'w') as fout:
            fout.write(decrypt_msg(msg))

        print("파일 복호화 성공\n")
        
    elif(selection == '3'):
        msg = input("암호화할 메시지\n")
        print(f"\n 암호화된 메시지: {encrypt_msg(msg)}")

    elif(selection == '4'):
        msg = input("복호화할 메시지\n")
        print(f"\n 복호화된 메시지: {decrypt_msg(msg)}")
    
    elif(selection == '5'):
            break
    
    else:
        print("잘못된 입력입니다.")