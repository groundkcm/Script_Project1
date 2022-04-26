import os
import re
import tkinter
import zipfile
import shutil

# 디버그 기능 추가 이미 파일있으면, 학기와 강의이름 tkinter에서 입력받기

# try:
#     pass
# except:
#     pass

my_lectures = ['3D 게임 프로그래밍', 'STL', '네트워크 기초', '선형대수학', '스크립터 언어', '인간과 철학']
normal_folders = ['doc', 'ppt', 'pdf', 'hwp', 'jpg', 'png']

l3d = re.compile(r''' (3d|3D)? (game|Game)[ ]?(Programming|programming)|게임[ ]?프로그래밍 ''', re.VERBOSE)
lstl = re.compile(r''' stl|STL ''', re.VERBOSE)
lnw = re.compile(r''' network|네트워크[ ]?기초?|Network ''', re.VERBOSE)
lln = re.compile(r''' linear|선형(대)?[ ]?수학?|Linear ''', re.VERBOSE)
lsc = re.compile(r''' script|스크립트[ ]?언어|Script ''', re.VERBOSE)
lhp = re.compile(r''' 인간과[ ]?철학|인철 ''', re.VERBOSE)

def make_lecture_folders():
    if os.path.exists('/Lab/Univ/3-1'):

        shutil.rmtree('/Lab/Univ/3-1')
        os.makedirs('/Lab/Univ/3-1')

        os.chdir('/Lab/Univ/3-1')
    else:
        os.makedirs('/Lab/Univ/3-1')
        os.chdir('/Lab/Univ/3-1')

    for lecture in my_lectures:
        if os.path.exists(lecture):
            continue
        os.mkdir(lecture)


def make_normal_folders():
    pass


def move_files():
    os.chdir('/Users/karam/Downloads')
    file_list = []
    for file in file_list:
        if l3d.search(file):
            shutil.move(file, '/Lab/Univ/3-1/3d 게임 프로그래밍')
        elif lstl.search(file):
            shutil.move(file, '/Lab/Univ/3-1/STL')
        elif lnw.search(file):
            shutil.move(file, '/Lab/Univ/3-1/네트워크 기초')
        elif lln.search(file):
            shutil.move(file, '/Lab/Univ/3-1/선형대수학')
        elif lsc.search(file):
            shutil.move(file, '/Lab/Univ/3-1/스크립트 언어')
        elif lhp.search(file):
            shutil.move(file, '/Lab/Univ/3-1/인간과 철학')


make_lecture_folders()
make_normal_folders()

# 실시간 반복
move_files()