from datetime import datetime

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

url = "http://eng.koreabaseball.com/Schedule/DailySchedule.aspx"

# 웹 페이지 열기
driver.get(url)

# WebDriverWait 객체 생성
wait = WebDriverWait(driver, 10)


# 현재 월을 얻는 함수
def get_current_month():
    element = wait.until(
        EC.presence_of_element_located((By.ID, 'cphContainer_cphContainer_cphContent_cphContent_lblGameMonth')))
    return int(element.text[6])


# 이전 달 버튼 클릭 함수
def click_goback_month():
    goback_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'prev')))
    goback_button.click()


# 다음 달 버튼 클릭 함수
def click_gonext_month():
    gonext_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'next')))
    gonext_button.click()


# 현재 월 확인 및 3월로 이동
while True:
    current_month = get_current_month()

    if current_month == 3:
        break

    click_goback_month()
    time.sleep(1)

current_year = datetime.now().year

for i in range(6):
    # tbody 요소 찾기
    tbody_element = driver.find_element(By.CSS_SELECTOR, "tbody")  # CSS 선택자 사용 예시

    # tbody 요소 하위 요소 (tr) 찾기
    rows = tbody_element.find_elements(By.TAG_NAME, "tr")

    date = ''

    # 각 행 데이터 추출 및 출력
    for row in rows:
        cells = row.find_elements(By.TAG_NAME, "td")
        row_data = [cell.text for cell in cells]
        if len(row_data) == 10:
            date = row_data[0]

        date_str = date
        date_parts = date_str.split('.')
        month = int(date_parts[0])
        day = int(date_parts[1][:2])
        current_year = datetime.now().year

        date_obj = datetime(current_year, month, day)
        formatted_date = date_obj.strftime('%Y-%m-%d')

        if len(row_data) == 10:
            row_data.pop(0)
            row_data.pop(0)

        row_data.insert(0, formatted_date)

        print(row_data)

    click_gonext_month()

# 웹 드라이버 종료
driver.quit()