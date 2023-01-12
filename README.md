구현 기능 목록
- 채팅 로비에서 유저수 노출
- 채팅방에서 마지막 유저가 나가면 채팅방 자동 삭제
- 각 메세지에 시각, 유저명, 유저 아바타 노출
- 채팅방에 새로운 유저가 들어오면, 최근 메세지 5개 보여주기
- 메세지 수정/삭제
- 메세지 입력 중에 "{유저명}님이 메세지 입력 중입니다." 메세지
- 메세지 리액션 : 좋아요.
- 파일/사진 업로드
- 채팅방에 비밀번호 설정하기
- 채팅방 입장신청하고, 허용한 유저만 입장하기
- 유저 로그아웃 시에, 참여 중인 채팅방에서 자동 나가기

보안
- 웹소켓 CSRF 보안
- OriginValidator 설정 테스트 (pytest)