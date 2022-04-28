import os
import re
import tkinter
import shutil
import datetime
import zipfile
from pptx import Presentation
import PyPDF2


# 디버그 기능 추가 이미 파일있으면, 학기와 강의이름 tkinter에서 입력받기

# try:
#     pass
# except:
#     pass

my_lectures = ['3D 게임 프로그래밍', 'STL', '네트워크 기초', '선형대수학', '스크립터 언어', '인간과 철학']
normal_folders = ['docx', 'pptx', 'pdf', 'hwp', 'jpg', 'png', 'txt']

# 다시 체크

l3d = re.compile(r'(3d|3D)?((game|Game)[ ]?(Programming|programming)|게임[ ]?프로그래밍)(DirectX|Direct3D)?')
lstl = re.compile(r'stl|STL')
lnw = re.compile(r'network|네트워크[ ]?기초?|Network')
lln = re.compile(r'linear|선형(대)?[ ]?수학?|Linear')
lsc = re.compile(r'(script|스크립트[ ]?언어|Script)(Python|python|pycharm|Pycharm)?(.py)?')
lhp = re.compile(r'인간과[ ]?철학|인철|철학')


def make_lecture_folders():
    if os.path.exists('/Lab/Univ/3-1'):
        os.chdir('/Lab/Univ/3-1')
    else:
        os.makedirs('/Lab/Univ/3-1')
        os.chdir('/Lab/Univ/3-1')

    for lecture in my_lectures:
        if os.path.exists(lecture):
            continue
        os.mkdir(lecture)


def make_normal_folders():
    if os.path.exists('/Lab/Files'):
        os.chdir('/Lab/Files')
    else:
        os.makedirs('/Lab/Files')
        os.chdir('/Lab/Files')

    for category in normal_folders:
        if os.path.exists(category):
            continue
        os.mkdir(category)


def move_files():
    os.chdir('/Users/karam/Downloads')
    now = datetime.datetime.today().strftime('%y%m%d')

    file_list = []
    # 오늘 다운받은 파일만 해당
    for file in os.listdir():
        abs_path = os.path.abspath(file)
        ctime = os.path.getctime(abs_path)
        cdate = datetime.datetime.fromtimestamp(ctime).strftime('%y%m%d')
        if cdate == now:
            file_list.append(file)

    for file in file_list:
        print(file)
        result = []

        if file.endswith('.pdf'):
            pass
        elif file.endswith('.pptx'):
            prs = Presentation(file)
            for slide in prs.slides:
                for shape in slide.shapes:
                    if not shape.has_text_frame:
                        continue
                    for paragraph in shape.text_frame.paragraphs:
                        result.append(paragraph.text)
        elif file.endswith('.txt'):
            pass
        else:
            result.append(file)

        for word in result:
            if lstl.search(word):
                # shutil.move(file, '/Lab/Univ/3-1/STL')
                shutil.copy(file, '/Lab/Univ/3-1/STL')
            elif l3d.search(word):
                # shutil.move(file, '/Lab/Univ/3-1/3d 게임 프로그래밍')
                shutil.copy(file, '/Lab/Univ/3-1/3d 게임 프로그래밍')
            elif lnw.search(word):
                # shutil.move(file, '/Lab/Univ/3-1/네트워크 기초')
                shutil.copy(file, '/Lab/Univ/3-1/네트워크 기초')
            elif lln.search(word):
                # shutil.move(file, '/Lab/Univ/3-1/선형대수학')
                shutil.copy(file, '/Lab/Univ/3-1/선형대수학')
            elif lsc.search(word):
                # shutil.move(file, '/Lab/Univ/3-1/스크립트 언어')
                shutil.copy(file, '/Lab/Univ/3-1/스크립트 언어')
            elif lhp.search(word):
                # shutil.move(file, '/Lab/Univ/3-1/인간과 철학')
                shutil.copy(file, '/Lab/Univ/3-1/인간과 철학')


if os.path.exists('/Lab'):
    shutil.rmtree('/Lab')

make_lecture_folders()
make_normal_folders()

# 실시간 반복
move_files()