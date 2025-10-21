#!/bin/bash

# 2부터 9까지 반복 (app2.py 부터 app9.py까지 처리)
for i in {2..9}; do 
    # 숫자가 한 자리인 경우 앞에 '0'을 붙여 두 자리로 만듦
    OLD_NAME="app/app${i}.py"
    NEW_NAME="app/app0${i}.py"
    
    # Git mv 실행
    git mv "$OLD_NAME" "$NEW_NAME"
done

echo "파일 이름 변경 및 Git 스테이징 완료."
