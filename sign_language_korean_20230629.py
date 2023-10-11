# -*- coding: utf-8 -*-
"""
Created on Wed Jun 28 23:55:57 2023

@author: KIBWA_23
"""

import cv2
import mediapipe as mp
import numpy as np
import keyboard
import time
from PIL import ImageFont, ImageDraw, Image
from hangul_utils.unicode import join_jamos

max_num_hands = 1

gesture = {
    0:'ㄱ', 1:'ㄴ', 2:'ㄷ', 3:'ㄹ', 4:'ㅁ', 5:'ㅂ', 6:'ㅅ', 7:'ㅇ',
    8:'ㅈ', 9:'ㅊ', 10:'ㅋ', 11:'ㅌ', 12:'ㅍ', 13:'ㅎ',
    14:'ㅏ', 15:'ㅑ', 16:'ㅓ', 17:'ㅕ', 18:'ㅗ', 19:'ㅛ', 20:'ㅜ', 21:'ㅠ',
    22:'ㅡ', 23:'ㅣ', 24:'ㅐ', 25:'ㅒ', 26:'ㅔ', 27:'ㅖ', 28:'ㅚ', 29:'ㅟ', 30:'ㅢ',
    31:'space', 32:'clear', 33:'backspace', 34:'shift'
}

mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
hands = mp_hands.Hands(
    max_num_hands=max_num_hands,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5)

file = np.genfromtxt('dataSetKorean.txt', delimiter=',')
angleFile = file[:, :-1]
labelFile = file[:, -1]
angle = angleFile.astype(np.float32)
label = labelFile.astype(np.float32)
knn = cv2.ml.KNearest_create()
knn.train(angle, cv2.ml.ROW_SAMPLE, label)
cap = cv2.VideoCapture(0)

startTime = time.time()
prev_index = 0
sentence = ''
recognizeDelay = 1

# 한글 폰트 경로
font_path = 'fonts/D2Coding.ttc'

# 한글 폰트 설정
font_size = 30
font = ImageFont.truetype(font_path, font_size)

while True:
    ret, img = cap.read()
    if not ret:
        continue
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    result = hands.process(imgRGB)
    
    # PIL 이미지 생성
    pil_image = Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    draw = ImageDraw.Draw(pil_image)
    
    if result.multi_hand_landmarks is not None:
        for res in result.multi_hand_landmarks:
            joint = np.zeros((21, 3))
            for j, lm in enumerate(res.landmark):
                joint[j] = [lm.x, lm.y, lm.z]

            v1 = joint[[0, 1, 2, 3, 0, 5, 6, 7, 0, 9, 10, 11, 0, 13, 14, 15, 0, 17, 18, 19], :]
            v2 = joint[[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20], :]

            v = v2 - v1
            v = v / np.linalg.norm(v, axis=1)[:, np.newaxis]
            compareV1 = v[[0, 1, 2, 4, 5, 6, 7, 8, 9, 10, 12, 13, 14, 16, 17], :]
            compareV2 = v[[1, 2, 3, 5, 6, 7, 9, 10, 11, 13, 14, 15, 17, 18, 19], :]
            angle = np.arccos(np.einsum('nt,nt->n', compareV1, compareV2))

            angle = np.degrees(angle)
            data = np.array([angle], dtype=np.float32)
            ret, results, neighbours, dist = knn.findNearest(data, 3)
            index = int(results[0][0])
            if index in gesture.keys():
                if index != prev_index:
                    startTime = time.time()
                    prev_index = index
                else:
                    if time.time() - startTime > recognizeDelay:
                        if index == 31:
                            sentence += ' '
                        elif index == 32:
                            sentence = ''
                        elif index == 33:
                            sentence = sentence[:-1]
                        elif index == 34:
                            # 'shift' 키에 대한 동작 수행
                            last_char = sentence[-1]
                            if last_char in ['ㄱ', 'ㄷ', 'ㅂ', 'ㅅ', 'ㅈ']:
                                shifted_char = chr(ord(last_char) + 1)
                                sentence = sentence[:-1] + shifted_char
                        else:
                            sentence += gesture[index]
            
                        print(sentence)
                        startTime = time.time()


                
                # 텍스트 위치 설정
                text_position = (int(res.landmark[0].x * img.shape[1] - 10),
                                 int(res.landmark[0].y * img.shape[0] + 40))
                text_color = (255, 255, 255)
                text_thickness = 3

                # 텍스트 그리기
                draw.text(text_position, gesture[index].upper(), font=font, fill=text_color,
                          stroke_width=text_thickness)
    
    # 텍스트 위치 설정
    text_position_1 = (20, 440)
    text_color_1 = (255, 255, 255)
    text_thickness_1 = 3

    # 텍스트 그리기
    draw.text(text_position_1, sentence, font=font, fill=text_color_1, stroke_width=text_thickness_1)

    # OpenCV 이미지로 변환
    img = cv2.cvtColor(np.array(pil_image), cv2.COLOR_RGB2BGR)
    
    if result.multi_hand_landmarks is not None:
        mp_drawing.draw_landmarks(img, res, mp_hands.HAND_CONNECTIONS)
    
    cv2.imshow('HandTracking', img)
    cv2.waitKey(1)
    if keyboard.is_pressed('b'):  # b를 누를시 프로그램 종료
        cap.release()
        cv2.destroyAllWindows()
        sentence = join_jamos(sentence)
        break
    

print(sentence)

import urllib.parse
import urllib.request
import json
from gtts import gTTS
from playsound import playsound
import os

client_id = "nqrRiDBAj1Ubev6cPx4L"
client_secret = "By4tMA1wAE"
encText = urllib.parse.quote(sentence)
data = "source=ko&target=en&text=" + encText
url = "https://openapi.naver.com/v1/papago/n2mt"
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
response = urllib.request.urlopen(request, data=data.encode("utf-8"))
rescode = response.getcode()


if(rescode==200):
    response_body = response.read()
    res = json.loads(response_body.decode('utf-8'))
    print(res['message']['result']['translatedText']) #res는result의 약자
    translated_text = res['message']['result']['translatedText']  # 번역 결과 추출
        
    tts = gTTS(text=translated_text, lang='en')  # 번역된 텍스트를 한국어 음성으로 변환
    if os.path.isfile('outputKoreanToEnglish.mp3'): os.remove('outputKoreanToEnglish.mp3')# 기존 파일삭제
            
    tts.save("outputKoreanToEnglish.mp3")  # 음성 파일 저장
        
else:
    print("Error Code:" + rescode)
            
playsound("outputKoreanToEnglish.mp3")  # 음성 파일 재생