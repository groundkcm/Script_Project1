import os
import re
import tkinter
import zipfile

# 디버그 기능 추가 이미 파일있으면, 학기와 강의이름 tkinter에서 입력받기

# try:
#     pass
# except:
#     pass

my_lectures = ['3D 게임 프로그래밍', 'STL', '네트워크 기초', '선형대수학', '스크립터 언어', '인간과 철학']
normal_folders = ['doc', 'ppt', 'pdf', 'hwp', 'jpg', 'png']


def make_lecture_folders():
    if os.path.exists('/Univ/3-1'):
        os.chdir('/Univ/3-1')
    else:
        os.mkdir('/Univ/3-1')
        os.chdir('/Univ/3-1')

    for lecture in my_lectures:
        if os.path.exists(lecture):
            continue
        os.mkdir(lecture)


def make_normal_folders():
    pass


def move_files():
    os.chdir('/Users/karam/Downloads')
    file_list = []


make_lecture_folders()
make_normal_folders()

# 실시간 반복
move_files()