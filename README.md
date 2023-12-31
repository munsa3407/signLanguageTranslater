# 수화 번역 프로젝트

## 소개

**mediapipe 라이브러리 기반 수화번역프로그램 AI 프로젝트**

이 프로젝트는 청각장애인들을 위한 현대적이고 편리한 수화 번역 서비스를 제공하기 위해 시작되었습니다. 수화는 한국어 지문자(자모음) 수화를 영어 음성으로, 영어 알파벳 수화를 한국어 음성으로 변환하는 기능을 제공합니다. 이 프로젝트는 Google의 mediapipe 라이브러리를 기반으로 하여 더욱 정확하고 실용적인 수화 번역을 지향합니다.


## 기획 의도

우리는 코로나 방역 방송 등 다양한 매체에서 수화를 통한 소통의 필요성을 느끼고, 이를 일상에서 더욱 효과적으로 활용할 수 있는 수화 번역 프로그램을 개발하고자 합니다. 이 프로젝트의 목적은 공식 석상 등 중대한 장소 뿐만 아니라, 일상에서도 손쉽게 활용 가능한 수화 번역 서비스를 제공하여 청각장애인들의 소통과 이해를 촉진하는 데 있습니다.

---

## 설치 가이드

프로젝트를 실행하기 전에 mediapipe 라이브러리를 설치해야 합니다. 아래는 설치 단계입니다.

1. **Python 설치:**
   - 프로젝트는 Python 언어로 작성되었습니다. Python이 설치되어 있지 않다면 [Python 공식 웹사이트](https://www.python.org/)에서 최신 버전을 다운로드하여 설치하세요.

2. **mediapipe 설치:**
   - 터미널 또는 명령 프롬프트를 열고 다음 명령어를 실행하여 mediapipe 라이브러리를 설치하세요.
     ```
     pip install mediapipe
     ```

3. **프로젝트 클론:**
   - 이제 프로젝트를 클론하거나 다운로드하여 로컬 환경에 가져옵니다.

4. **의존성 설치:**
   - 프로젝트 루트 디렉토리에서 다음 명령어를 실행하여 필요한 의존성을 설치하세요.
     ```
     pip install -r requirements.txt
     ```

5. **프로젝트 실행:**
   - 데이터셋이 이미 생성되었다면 아래 사용법을 참고하여 프로젝트를 실행할 수 있습니다.

---

## 사용법

프로젝트의 사용법은 다음과 같습니다:

1. **데이터셋 생성:**
   - 프로젝트 루트 디렉토리에서 `dataset_maker.py`를 실행하여 데이터셋을 생성할 수 있습니다.
     ```
     python DataSet_Maker.py
     ```
     데이터셋은 txt 파일로 생성되며, 차후 데이터셋을 이용하기 위해 txt 파일명을 바꿔주거나 코드 속 txt 파일을 바꿔주면 됩니다.

2. **영어 수화 프로그램 실행:**
   - 데이터셋이 만들어진 후(dataSetEnglish.txt), `sign_language_english_20230628.py`를 실행하여 영어 수화 프로그램을 시작할 수 있습니다.
     ```
     python sign_language_english_20230628.py
     ```

3. **한국어 수화 프로그램 실행:**
   - 데이터셋이 만들어진 후(dataSetKorean.txt), `sign_language_korean_20230629.py`를 실행하여 한국어 수화 프로그램을 시작할 수 있습니다.
     ```
     python sign_language_korean_20230629.py
     ```

4. **수어 정확도 분석:**
   - `수어정확도분석.py`를 실행하여 수어 정확도를 분석할 수 있습니다.
     ```
     python 수어 정확도 분석.py
     ```

5. **사이트 접속:**
   - flask로 구현된 웹페이지를 접속할 수 있습니다.
     ```
     python flaskapp.py
     ```
     혹은
     ``` 
     python flaskappHand.py
     ```
---

##


프로젝트 사용 환경 및 라이브러리

[![Python](https://img.shields.io/badge/Python-3.6%2B-blue)](https://www.python.org/)
[![MediaPipe](https://img.shields.io/badge/MediaPipe-0.8.3%2B-brightgreen)](https://google.github.io/mediapipe/)
[![Flask](https://img.shields.io/badge/Flask-2.0%2B-blue)](https://flask.palletsprojects.com/en/2.0.x/)
[![HTML](https://img.shields.io/badge/HTML-5-orange)](https://developer.mozilla.org/en-US/docs/Web/Guide/HTML/HTML5)
[![CSS](https://img.shields.io/badge/CSS-3-blueviolet)](https://developer.mozilla.org/en-US/docs/Web/CSS)
[![Hangul_Utils](https://img.shields.io/badge/Hangul_Utils-1.1-green)](https://pypi.org/project/hangul-utils/)
[![OpenCV](https://img.shields.io/badge/OpenCV-4.5%2B-yellow)](https://opencv.org/)


