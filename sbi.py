from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium.webdriver.support.ui import Select
from pynput.keyboard import Key,Controller


driver = webdriver.Chrome()

driver.maximize_window()

driver.get("https://sbiluatposservices.sbilife.co.in/MconnectDemo/#/Pre/login")

wait = WebDriverWait(driver, 8)

username_field = wait.until(EC.element_to_be_clickable((By.NAME, "edt_usercode")))  
driver.execute_script("arguments[0].scrollIntoView();", username_field)

username_field.send_keys("990134795")  
password_field = wait.until(EC.element_to_be_clickable((By.NAME, "password")))  
driver.execute_script("arguments[0].scrollIntoView();", password_field)

password_field.send_keys("sbil")  
login_button = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/app-root/app-auth-user/app-login/div/body/div[1]/div[2]/div[2]/form/ul/li[2]/div/input")))
login_button.click()
time.sleep(5)

need_analysis = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/app-root/app-dashboard/app-home-screen/body/div[4]/div/div[3]/div[3]/div/div")))
need_analysis.click()
time.sleep(2)

start_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "mdc-button__label")))
start_button.click()
time.sleep(5)

first_name_field = wait.until(EC.element_to_be_clickable((By.ID, "Fname")))
first_name_field.send_keys("Supriya")  # Entering dummy data

middle_name_field = wait.until(EC.element_to_be_clickable((By.ID, "mat-input-1")))
middle_name_field.send_keys("Raj")  # Entering dummy data


last_name_field = wait.until(EC.element_to_be_clickable((By.ID, "Lname")))
last_name_field.send_keys("Morankar")  # Entering dummy data

Mobile_number = wait.until(EC.element_to_be_clickable((By.ID, "str_mobile_number")))
Mobile_number.send_keys("98341235595") 

dob_field = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="mat-input-4"]')))
dob_field.send_keys("09101975") 

time.sleep(1)

toggle_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//span[@class='mat-button-toggle-label-content' and text()='Form60']"))
)

toggle_button.click()
time.sleep(2)

# adhar_field = wait.until(EC.element_to_be_clickable((By.ID, 'mat-input-6')))
# adhar_field.send_keys("622358427785") 

email = wait.until(EC.element_to_be_clickable((By.ID, 'mat-input-7')))
email.send_keys("sup@gmail.com") 

# time.sleep(2)
acount_number = wait.until(EC.element_to_be_clickable((By.ID, 'EC_accountNumber')))
acount_number.send_keys("123456789")

# time.sleep(2)

ifscCode = wait.until(EC.element_to_be_clickable((By.ID, 'EC_ifscCode')))
ifscCode.send_keys("SBIN0006070")


time.sleep(5)
proceed_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='next-back-button']//button//span[text()='Proceed']")))

proceed_button.click()
time.sleep(10)

ok_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "ok-button")))
ok_button.click()
time.sleep(5)


# elements = driver.find_elements(By.XPATH, "//input[@id='mat-radio-12-input']")
# print(f"Found {len(elements)} elements.")

# Find the element
radio_button = driver.find_element(By.XPATH, "//input[@id='mat-radio-12-input']")
driver.execute_script("arguments[0].click();", radio_button)
time.sleep(5)


radio_button_single = driver.find_element(By.XPATH, "//input[@id='mat-radio-17-input']")
driver.execute_script("arguments[0].click();", radio_button_single)
time.sleep(5)

dropdown_education = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='mat-mdc-select-trigger ng-tns-c1154042729-14']")))
dropdown_education.click()
time.sleep(2)

option_education = wait.until(EC.element_to_be_clickable((By.XPATH, "//mat-option//span[contains(text(), 'Post Graduate/ Professional')]")))
option_education.click()
time.sleep(2)

dropdown_occupation = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='mat-mdc-select-trigger ng-tns-c1154042729-16']")))
dropdown_occupation.click()
time.sleep(2)

option_occupation = wait.until(EC.element_to_be_clickable((By.XPATH, "//mat-option//span[contains(text(), 'Organised pvt sector')]")))
option_occupation.click()
time.sleep(2)


annual_income = wait.until(EC.element_to_be_clickable((By.ID, "propAnnualIncome")))
annual_income.send_keys("1200000")
time.sleep(2)

dropdown_invest = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='mat-mdc-select-trigger ng-tns-c1154042729-32']")))
dropdown_invest.click()

option_invest = wait.until(EC.element_to_be_clickable((By.XPATH, "//mat-option//span[contains(text(), '> 5 Years')]")))
option_invest.click()
time.sleep(2)

annual_exp = wait.until(EC.element_to_be_clickable((By.ID, "annExp")))
annual_exp.send_keys("1200000")
time.sleep(2)

annual_sav = wait.until(EC.element_to_be_clickable((By.ID, "accSav")))
annual_sav.send_keys("15000")
time.sleep(2)

dropdown = wait.until(EC.element_to_be_clickable((By.XPATH, "//mat-select[@id='propPopCat']")))
dropdown.click()
time.sleep(2)

option = wait.until(EC.element_to_be_clickable((By.XPATH, "//mat-option//span[contains(text(), 'Metro')]")))
option.click()
time.sleep(2)


radio_self = driver.find_element(By.XPATH, "//input[@id='mat-radio-5-input']")
driver.execute_script("arguments[0].click();", radio_self)
time.sleep(5)

# radio_yes = driver.find_element(By.XPATH, "//input[@id='mat-radio-8-input']")
# driver.execute_script("arguments[0].click();", radio_yes)
# time.sleep(5)


dropdown_xpath = "//div[@class='mat-mdc-select-trigger ng-tns-c1154042729-37']"
dropdown_proof = wait.until(EC.element_to_be_clickable((By.XPATH, dropdown_xpath)))
dropdown_proof.click()
time.sleep(2)  

option_xpath = "//mat-option//span[contains(text(), 'Birth Certificate')]"
option_proof = wait.until(EC.element_to_be_clickable((By.XPATH, option_xpath)))
option_proof.click()
time.sleep(2)  

button_touch_target = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id=\"cdk-step-content-0-0\"]/app-financial-goals/div/form/div/div/app-phy-ovd/div/div/div[1]/div/div/div[2]/button/span[4]")))
button_touch_target.click()
time.sleep(2)

confirm_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//app-action-alert-popup//button/span[text()=' No ']")))
confirm_button.click()
time.sleep(2)
keyboard= Controller()
keyboard.type("C:\\Users\\admin\\Pictures\\Screenshots\\Screenshot (1).png")
keyboard.press(Key.enter)
time.sleep(2)

button_preview = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='modal-component']/div/div/app-upload-popup/mat-dialog-actions[2]/button[2]/span[4]")))
driver.execute_script("arguments[0].click();", button_preview)

time.sleep(2)

button_upload = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id=\"modal-component\"]/div/div/app-upload-popup/mat-dialog-actions/button[2]/span[4]")))
driver.execute_script("arguments[0].click();", button_upload)

time.sleep(5)



dropdown_id = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='mat-select-value-15']")))
dropdown_id.click()
time.sleep(2)

# Wait for the desired option to be visible and click it
option_id = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'NREGA Job Card')]")))
option_id.click()
time.sleep(2)

keyboard= Controller()
keyboard.type("C:\\Users\\admin\\Pictures\\Screenshots\\Screenshot (1).png")
keyboard.press(Key.enter)
time.sleep(2)


button_id = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='cdk-step-content-0-0']/app-financial-goals/div/form/div/div/app-phy-ovd/div/div/div[2]/div/div/div[2]/button/span[4]")))
button_id.click()
time.sleep(5)


confirm_button_no = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@class='mdc-button mdc-button--raised mat-mdc-raised-button mat-unthemed mat-mdc-button-base ng-star-inserted']/span[@class='mdc-button__label' and text()=' No ']")))
confirm_button_no.click()
time.sleep(5)

keyboard= Controller()
keyboard.type("C:\\Users\\admin\\Pictures\\Screenshots\\Screenshot (1).png")
keyboard.press(Key.enter)
time.sleep(2)

button_preview = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'mat-mdc-button')]/span[@class='mdc-button__label' and text()='Preview']")))
driver.execute_script("arguments[0].click();", button_preview)
time.sleep(2)

button_upload_id = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='modal-component']/div/div/app-upload-popup/mat-dialog-actions/button[2]/span[4]")))
driver.execute_script("arguments[0].click();", button_upload_id)
time.sleep(5)

next_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='next-back-button ng-star-inserted']//button//span[text()='Next']")))
next_button.click()
time.sleep(2)

protection_health_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='example-box ng-star-inserted']//p[text()='Protection or Health Cover']")))
protection_health_button.click()
time.sleep(2)

wealth_creation_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='example-box ng-star-inserted']//p[text()='Wealth Creation or Insurance savings']")))
wealth_creation_button.click()
time.sleep(2)


insurance_regular_income_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='example-box ng-star-inserted']//p[text()='Insurance for Regular Income']")))
insurance_regular_income_button.click()
time.sleep(2)

retirement_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='example-box ng-star-inserted']//p[text()='Retirement']")))
retirement_button.click()
time.sleep(5)

# next_button1 = wait.until(
#     EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'mdc-button') and contains(span/text(), 'Next')]"))
# )
# next_button1.click()
# next_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[contains(@class, 'next-back-button')]//button[span[text()='Next']]")))
# next_button.click()
# time.sleep(2)

# next_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='cdk-step-content-1-1']/div/button[2]")))
# next_button.click()

# time.sleep(3)

element = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='col-md-2 ng-star-inserted']//div[@class='recommendation-product']//p[contains(text(), 'eShield Next')]")))
element.click()

time.sleep(3)


# select_plan = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@id='mat-select-value-44']")))
# select_plan.click()
# time.sleep(3)

# # Wait for the desired option to be visible and click it
# plan_option = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Level Cover')]")))
# plan_option.click()
# time.sleep(2)


select_plan_dropdown = wait.until(EC.element_to_be_clickable((By.XPATH, "//mat-select[@formcontrolname='selPlan']")))
select_plan_dropdown.click()
time.sleep(2)
# Select an option from the dropdown
plan_option = wait.until(EC.element_to_be_clickable((By.XPATH, "//mat-option/span[contains(text(),'Level Cover')]")))  # Replace 'Your Option Text Here' with the actual text
plan_option.click()
time.sleep(2)

# Whole Life Dropdown
whole_life_dropdown = wait.until(EC.element_to_be_clickable((By.XPATH, "//mat-select[@formcontrolname='selWholeLife']")))
whole_life_dropdown.click()
time.sleep(2)

# Select an option from the dropdown
whole_life_option = wait.until(EC.element_to_be_clickable((By.XPATH, "//mat-option/span[contains(text(),'Whole Life')]")))  # Replace 'Your Option Text Here' with the actual text
whole_life_option.click()
time.sleep(2)

benifit_dropdown = wait.until(EC.element_to_be_clickable((By.XPATH, "//mat-select[@formcontrolname='selDeathBenPay']")))

# Click the dropdown to open options
benifit_dropdown.click()
time.sleep(2)

# Wait for options to be visible and select one (replace 'OPTION_TEXT' with actual value)
benifit_option = wait.until(EC.element_to_be_clickable((By.XPATH, "//mat-option//span[contains(text(),'Lump sum')]")))
benifit_option.click()
time.sleep(2)

next_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'next_btn')]")))

next_button.click()
time.sleep(3)


sum_assured_input = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='col_10']/div/div/div[2]/div[2]/div/input")))
sum_assured_input.send_keys("7500000")  # Enter your desired sum assured value
time.sleep(2)

calculate_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Calculate')]")))
calculate_button.click()
time.sleep(2)

proceed_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[span[text()='Proceed']]")))
proceed_button.click()
time.sleep(15)

add_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Add')]")))
add_button.click()
time.sleep(10)

add_to_cart_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[span[contains(text(), 'Add to Cart')]]")))
add_to_cart_button.click()
time.sleep(10)

proceed_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Proceed to Buy')]")))
proceed_button.click()
time.sleep(5)
