## Frontend app 사용방법

프로젝트 두들의 시작페이지 입니다.

1. 프로젝트의 루트디렉토리에서 `pip install -r requirements.txt`를 실행합니다.
2. `/frontend/app/` 디렉토리로 이동합니다.  
3. `main.py` 파일이 존재하는지 확인합니다.
4. `uvicorn main:app --reload` 를 통해 fastapi 서버를 실행합니다.
5. `http://127.0.0.1:8000` 에 브라우저를 통해 접속합니다.
6. 게임 시작을 누르면 캔버스가 나타나고 아무 그림을 그리면 `오리`라는 답변을 줍니다.