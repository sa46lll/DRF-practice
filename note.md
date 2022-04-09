### Django Rest Framework

>  DRF Router
- SimpleRouter
  - 표준 셋으로 list, create, retrieve, update, partial_update 그리고 destroy 작업에 대한 경로가 포함함
  - viewset은 @action 데코레이터를 사용하여 라우팅할 추가 메서드를 표시
- DefaultRouter
  - SimpleRouter과 유사하지만 모든 list views에 하이퍼링크를 포함하는 응답을 반환하는 기본 API Root view를 포함함
  - 포맷 스타일 형식을 접미사나 query_string에 대한 경로 생성
    - ex) localhost:8000/api2/users/ **?format=json**
    - localhost:8000/api2/users **.json**

> ViewSet
- 상속 관계
  - View > APIView > GenericAPIView
- ReadOnlyModelViewSet
  - 목록 조회 & 특정 레코드 조회 (get만 가능)
- ModelViewSet
  - 목록 조회 & 특정 레코드 생성/조회/수정/삭제 전부 자동으로 만들어 줌.
    - CreateAPIView
    - ListAPIView
    - RetrieveAPIView
    - UpdateAPIView
    - DestroyAPIView
  - ViewSet
    - 자동으로 만들지마! 내가 다 만들께
    - url당 하나의 테이블만 다룰 때 (그게 아니면 genericView 가 좋다.)
    - actions 인자 필수
      - router를 사용하면 알아서 인자를 채워줌

> GenericView
- 목록 조회
  - ListAPIView
    - PostSerializer(instance=, many=True)
- 특정 레코드 조회
  - RetrieveAPIView
    - PostSerializer(instance=, many=False)
- 특정 레코드 생성
  - CreateAPIView
- 특정 레코드 수정
  - UpdateAPIView
    - put: 리소스의 모든 것을 업데이트
    - patch: 리소스의 일부를 업데이트

> Serialization
- 직렬화 (read Operation)
  - GET
  - 과정
    - instance
    - Serializer(instance=XXX)
    - dict
    - json data
    - response
- 역직렬화 (write Operation)
  - POST, UPDATE, DELETE, PATCH
  - 과정
    - json data
    - dict
    - Serializer(data=XXX)
    - is_valid(), validated_data (유효성 검사)
    - instance
    - save()

> 참고문서
- [DRF 참고문서](https://www.cdrf.co/)
- [CBV 참고문서](https://ccbv.co.uk/)

> ###### 단축키
| description                  	 | KEY            	 |
|---------------------------------|------------------|
| 현재 기능 해제                  	 | Esc            	 |
| Code Completion                 	 | Ctrl + Space   	 |
| Code Completion and Import      	 | Ctrl + Space*2 	 |
| Comment toggle                  	 | Ctrl + /       	 |
| Copy                            	 | Ctrl + c       	 |
| Paste                           	 | Ctrl + v       	 |
| Cut                             	 | Ctrl + x       	 |
| Delete Line                     	 | Ctrl + y       	 |
| Duplicate Line                  	 | Ctrl + d       	 |
| Save all                        	 | Ctrl + s       	 |
| 찾기                            	 | Ctrl + f       	 |
| 바꾸기                          	  | Ctrl + r       	 |
| 정의한 곳으로 이동 (Ctrl+click) 	       | Ctrl + b       	 |
| 설정 (Settings)                 	| Ctrl + Alt + s     	|
| Navigate Back                   	| Ctrl + Alt + left  	|
| Navigate Forward                	| Ctrl + Alt + right 	|
| Multi cursor                    	| Alt + click        	|
| Multi cursor (VS Code)          	| Ctrl + click       	|


