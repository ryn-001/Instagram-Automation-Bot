import tkinter as tk
from tkinter import messagebox
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import pyautogui
import time

class Bot():
    def __init__(self):
        self.username = None
        self.password = None
        self.driver = None

    def start_browser(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def login(self):
        if self.driver is None:
            self.start_browser()

        self.driver.get('https://instagram.com')

        # Username
        try:
            username_input = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='username']"))
            )
            username_input.send_keys(self.username)

        except Exception as e:
            print(f"An error occurred: {e}")

        # Password
        try:
            password_input = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='password']")))
            password_input.send_keys(self.password)

        except Exception as e:
            print(f"An error occurred: {e}")

        # Clicking Login button
        try:
            login_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="loginForm"]/div/div[3]')))
            login_button.click()

        except Exception as e:
            print(f"An error occurred: {e}")

        # Clicking NotNow
        try:
            Not_Now = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/section/main/div/div/div/div/div')))
            Not_Now.click()

        except Exception as e:
            print(f"An error occurred: {e}")

        # Clicking NotNow1
        try:
            Not_Now1 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Not Now')]")))
            Not_Now1.click()

        except Exception as e:
            print(f"An error occurred: {e}")

        # Clicking AutoPost
        try:
            self.driver.get('https://www.instagram.com/ctrl.geeks001/')

            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

            Share_first_Post = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[@aria-label='New post']")))
            Share_first_Post.click()

            Select_from_computer = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[6]/div[1]/div/div[3]/div/div/div/div/div/div/div/div[2]/div[1]/div/div/div[2]/div/button")))
            Select_from_computer.click()

        except Exception as e:
            print(f"An error occurred: {e}")

        # Post
        try:
            Select_from_computer = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[6]/div[1]/div/div[3]/div/div/div/div/div/div/div/div[2]/div[1]/div/div/div[2]/div/button")))
            Select_from_computer.click()
            time.sleep(2)  
    
            pyautogui.write(r"E:\Aryan\Python Instagram Bot\Posts\dog meme.jpg")
            pyautogui.press('enter')

            time.sleep(2)
            pyautogui.write(r"dog meme")
            time.sleep(3)
            pyautogui.press('enter')

        except Exception as e:
            print(f"An error occurred: {e}")

        # Next 
        try:
            Next = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[6]/div[1]/div/div[3]/div/div/div/div/div/div/div/div[1]/div/div/div/div[3]/div")))
            Next.click()

            time.sleep(3)
            Next_ = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[6]/div[1]/div/div[3]/div/div/div/div/div/div/div/div[1]/div/div/div/div[3]/div")))
            Next_.click()

        except Exception as e:
            print(f"An error occurred : {e}")

        # Share
        try:
            time.sleep(5)
            share_button = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[6]/div[1]/div/div[3]/div/div/div/div/div/div/div/div[1]/div/div/div/div[3]/div/div")))
            share_button.click()
        except Exception as e:
            print(f"An error occurred: {e}")

        # Refresh
        time.sleep(5)
        self.driver.refresh()

    def close_browser(self):
        if self.driver:
            self.driver.quit()

class InstagramBotGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Instagram Bot")
        
        self.username_label = tk.Label(root, text="Username:")
        self.username_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")
        self.username_entry = tk.Entry(root)
        self.username_entry.grid(row=0, column=1, padx=10, pady=5)
        
        self.password_label = tk.Label(root, text="Password:")
        self.password_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")
        self.password_entry = tk.Entry(root, show="*")
        self.password_entry.grid(row=1, column=1, padx=10, pady=5)
        
        self.start_button = tk.Button(root, text="Start", command=self.start_bot)
        self.start_button.grid(row=2, column=0, padx=10, pady=5)
        
        self.stop_button = tk.Button(root, text="Stop", command=self.stop_bot)
        self.stop_button.grid(row=2, column=1, padx=10, pady=5)

        self.bot = Bot()

    def start_bot(self):
        self.bot.username = self.username_entry.get()
        self.bot.password = self.password_entry.get()
        self.bot.login()

    def stop_bot(self):
        self.bot.close_browser()

if __name__ == "__main__":
    root = tk.Tk()
    app = InstagramBotGUI(root)
    root.mainloop()
