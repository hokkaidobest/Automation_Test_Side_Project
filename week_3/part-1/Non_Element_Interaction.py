from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# Step 1 : Open the Chrome browser.
options = Options()
options.chrome_executable_path = "/usr/local/bin/chromedriver"
driver = webdriver.Chrome(options = options)

# Step 2 : Maximize the browser window.
driver.maximize_window()

# Step 3 : Navigate to Appworks School Website (https://school.appworks.tw).
driver.get("https://school.appworks.tw")

# Step 4 : 
# Print “PASS” if the title of the page matches with “Code Your Future” else “FAIL”.
if "Code Your Future" in driver.title:
    print("PASS")
else:
    print("FAIL")

# Step 5 : Click the link “AppWorks” in top right corner
element = driver.find_element(By.XPATH, '//*[@id="menu-item-2269"]/a')
element.click()

# Step 6 : Switch to new tabs to AppWorks website
handles = driver.window_handles
driver.switch_to.window(handles[1])

# Step 7 : Print “PASS” if there is text “By Founders, For Founders” else “FAIL”.
if "By Founders, For Founders" in driver.page_source:
    print("PASS")
else:
    print("FAIL")

# Step 8 : Navigate to https://appworks.tw/investments/
driver.get("https://appworks.tw/investments/")

# Step 9 : 
# Print “PASS” if there is text “We know you have a choice. We want you to choose us.” else “FAIL”.
if "We know you have a choice. We want you to choose us." in driver.page_source:
    print("PASS")
else:
    print("FAIL")

# Step 10 : Navigate back to the Appworks Website.
driver.back()

# Step 11 : Print the URL of the current page.
print(driver.current_url)

# Step 12 : Navigate forward.
driver.forward()

# Step 13 : Close the current window
driver.close()

# Step 14 : Switch back to the original window and reload the page.
driver.switch_to.window(handles[0])
driver.refresh()

# Step 15 : Finally, Close the Browser.
driver.quit()