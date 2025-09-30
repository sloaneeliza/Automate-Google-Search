from selenium import webdriver
from selenium.webdriver.chrome.service import Service


def append_text_to_file(filename, text_to_append):
    try:
        with open(filename, 'a') as file:
            text = text_to_append.replace('+', ' ')
            text = text.replace('Stop', '')
            file.write(text_to_append + '\n')
        print(f"Text appended to {filename} successfully.")
    except Exception as e:
        print(e)

def searches():
    print("Welcome to Google Automated Search. Type any searches you want to find. To stop, type 'Stop'.")
    result_list = []


    while True:
        user_input = input("Enter a search query: ")
        if user_input == "Stop":
            browser.quit()
            break
        else:
            result_list.append(user_input)
            service = Service("chromedriver.exe")
            browser = webdriver.Chrome(service=service)

            browser.get(f"https://www.google.com/search?q={user_input}")
            filename = 'searches.txt'
            append_text_to_file(filename, user_input)
    print(result_list)



searches()



