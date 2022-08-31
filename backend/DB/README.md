# Build mocking DB on local host

테스트 환경을 위해 `postgresql`을 이용하여 로컬 DB를 구축하는 스크립트 입니다.

## Install
1. 먼저 docker를 로컬 환경에 맞게 설치합니다.  
2. `build_mockingDB_container.sh`를 실행합니다.
3. `psql` 도커 이미지가 없다면 이미지를 풀링하여 가지고 옵니다. 이미지가 있다면 생략하고 진행됩니다.
4. 컨테이너가 이미 있다면 기존의 컨테이너를 지우고 새로 만들지 물어봅니다.
5. 컨테이너 빌드가 끝나면 `psql` 접속을 확인하고 종료합니다.

## Connect
1. 위의 `Install`을 진행합니다.
2. `.env` 환경변수로 만들어진 컨테이너가 떠있는지 확인합니다.
3. 컨테이너가 있는 상태에서 `connect_mockDB.sh`를 실행합니다.