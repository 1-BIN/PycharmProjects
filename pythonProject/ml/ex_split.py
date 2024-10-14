# pip install split-folders
import splitfolders
# 하나의 폴더를 train/validation/test 분류 폴더로 분할해줍니다.
splitfolders.ratio('./whale', output='split_whale', ratio=(.8, .0, .2)) # default는 랜덤분류,
                                                                        # seed='?' 시드값 설정 시 고정되어 분류
