# 헤더 추가
from init import *



# 초기화 및 설정 - 시스템 정보 출력
import platform
import sys
print ("-------------------------------------")
print ("(2023) intelligentHumanoid HYMECADDIE")
print ("-------------------------------------")
os_version = platform.platform()
print (" ---> OS " + os_version)
python_version = ".".join(map(str, sys.version_info[:3]))
print (" ---> Python " + python_version)
opencv_version = cv2.__version__
print (" ---> OpenCV  " + opencv_version)


# 변수 초기화
tasks_count = 0  # 현재 작업의 상태를 나타내는 변수 초기화 



#메인 작업 루프
while True:
    CAMERA.show_image() 
    print('task_count: ', tasks_count)


    if tasks_count == 0:
        pass
        # 0. 초기 공 치는 작업 설정

    elif tasks_count == 1:
        pass
        # 1. 공 찾기

    elif tasks_count == 2:
        pass
        # 2. 공 접근

    elif tasks_count == 3:
        pass
        # 3. 홀에 들어갔는지 확인

    elif tasks_count == 4:
        pass
        # 4. 회전 (들어가지 않았을 경우)

    elif tasks_count == 5:
        pass
        # 5. 타격

