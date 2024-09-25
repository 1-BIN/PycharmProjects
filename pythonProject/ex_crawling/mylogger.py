import logging
# 로그파일 생성 라이브러리
# 소프트웨어나 시스템 실행 중 발생하는 이벤트를 시간 순서대로 기록한 파일
# 버그추적, 사용자 활동 모니터링 및 다양한 용도로 사용
# 로그 레벨(warnning, error, info, debug)

def make_logger(fileNm, name=None):
    # 로그 생성
    logger = logging.getLogger(name)
    # 레벨 설정(DEBUG로 설정하면 모두 처리됨)
    logger.setLevel(logging.DEBUG)
    # 출력 포맷 설정
    formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    # handler 설정
    console = logging.StreamHandler()                                         #콘솔출력입니다
    file_handler = logging.FileHandler(filename=fileNm, encoding="UTF-8")     #파일에 저장되는 내용입니다.
    # handler level 설정
    console.setLevel(logging.INFO)
    file_handler.setLevel(logging.DEBUG)
    # 출력포맷지정
    console.setFormatter(formatter)
    file_handler.setFormatter(formatter)
    logger.addHandler(console)
    logger.addHandler(file_handler)
    return logger

if __name__ == '__main__':
    log = make_logger("test.log", "mylogger.py")
    log.debug("debug test")
    log.info("info test")
    log.warning("warning!")
    log.error("error!!!!!!!!!!!!!!!!!!")

