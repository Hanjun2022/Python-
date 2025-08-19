from bs4 import BeautifulSoup
soup = BeautifulSoup("<p>Some<b>bad<i>HTML")
print(soup.prettify())

#pip list
#pip show 패키지명
#pip install --upgrade 패키지명 
#pop uninstall 패키지명 

# import random
# print(dir())

# print("===========")
# import pickle
# print(dir())

# list=[1,2,3,4,2]
# list.sort()
# list.reverse()

# list.remove(2)
# print(list)
# # print(dir(list))

# dir 이거는 내장함수가 무엇인지 알 수 있다. 
# name="KimJimin"
# print(dir(name))

# print(name.find("Kim"))

# glob. 현재 파일 경로 내의 폴더/ 파일 목록 조회 (윈도우 (dir<--- d))
import glob

print(glob.glob("*.py"))


# os : 운영체제에서 제공하는 기본 기능 
import os
folder ="prk.py"

if os.path.exists(folder):
    print("이미 존재하는 폴더입니다.")
    os.rmdir(folder)
    print(folder,"폴더를 삭제하였습니다.")
else:
    os.makedirs(folder)
    print(folder,"폴더를 생성하였습니다.")

if os.path.exists(folder):
    if os.path.isdir(folder): # 폴더인지 확인
        os.rmdir(folder)
        print(f"'{folder}' 폴더가 삭제되었습니다.")
    elif os.path.isfile(folder): # 파일인지 확인
        os.remove(folder)
        print(f"'{folder}' 파일이 삭제되었습니다.")
    else:
        print("경로가 유효하지 않습니다.")