from google.oauth2.service_account import Credentials #  автентифікації та авторизації з Google API за допомогою облікових даних сервісного акаунта
import tkinter.messagebox as messagebox # повідомлення користувачу
from bs4 import BeautifulSoup # парсер
import tkinter as tk # дизайн
import gspread # для автомитизації та веб парсера
from selenium import webdriver 
from selenium.webdriver.common.by import By # пошку елементів на сторинці
from selenium.webdriver.chrome.service import Service # для керування послуги
import tkinter.scrolledtext as scrolledtext
import json
import os
try:



# scope визначає список дозволів, які запитуються від користувача при авторизації в Google API
    scope = ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive']

    # Цей код відповідає за авторизацію користувача та доступ до гугл-таблиці
    creds = Credentials.from_service_account_file('credentials2.json', scopes=scope) # credentials2.json сервісний файл Google Cloud
    with open('sheet_id.txt', 'r') as f:
        credentials = f.readlines()

    sheet_id = credentials[0].strip() # Зчитування 4-го рядка та видалення зайвих символів

    # sheet_id = '1ZKJwqgzrZ6Wux0tbwW5e0v7m6g1o0KiFjqV0FPP2WtU' # посилання на таблицю 
    client = gspread.authorize(creds)
    sheet = client.open_by_key(sheet_id).sheet1



    # авторизація на сайт мудла
    def login(username, password):
        s = Service('chromedriver.exe') # використання хром драйвера (помістити в тому ж каталозі файла)
        driver = webdriver.Chrome(service=s)
        driver.get('https://edu.regi.rovno.ua/login') # передрисація на сайт
        driver.minimize_window() # скриває вікно від користувача
        username_field = driver.find_element(By.NAME, 'username') #пошук елементу імя
        username_field.send_keys(username)#передаємо пароль (з файлу credentials.txt)
        password_field = driver.find_element(By.NAME,'password') #пошук елементу паролю
        password_field.send_keys(password)# передємо пароль з файлу
        login_button = driver.find_element(By.ID,'loginbtn') #пошук елементу кнопки
        login_button.click() #дія на кнопку
        driver.implicitly_wait(5)
        current_url = driver.current_url 
        print('Логін за посиланням:', current_url)

        if 'https://edu.regi.rovno.ua' in current_url:
            print('Ви успішно пройшли авторизацію!')
        else:
            print('Помилка авторизації...')

        return driver

    # заповнення даних: пароль, логіну, посилання за користувача з файлу
    def load_credentials():
        with open("credentials.txt", "r") as f:
            login, password, link = map(str.strip, f.readlines())
            username_entry.insert(0, login)
            password_entry.insert(0, password)
            link_entry.insert(0, link)

    # парсер оцінок з мудла
    def parser_grade(): # функція парсингу оцінок
        username, password, link, start_cell, end_cell = map(tk.Entry.get, (username_entry, password_entry, link_entry, start_cell_entry, end_cell_entry)) # отримання кінцевої комірки для запису даних з віджета
        driver = login(username, password) # вхід до системи з використанням вказаного логіну та паролю
        driver.get(link) # перехід за вказаним посиланням
        print("Переходжу за вашим посиланням: ", link)
        driver.minimize_window() # скриває вікно браузера від користувача
        html = driver.page_source # отримання HTML-коду сторінки
        soup = BeautifulSoup(html, 'html.parser') # створення об'єкту BeautifulSoup для парсингу HTML
        grade_table = soup.find('table', {'class': 'generaltable'}) # пошук таблиці з оцінками за класом 'generaltable'
        print('Пошук таблиці з оцінками...')
        rows = grade_table.findAll('tr') # отримання всіх рядків таблиці
        grades = [] # створення порожнього списку для збереження оцінок
        for row in rows: 
            cells = row.findAll('td') # отримання всіх комірок поточного рядка таблиці
            if len(cells) > 1:
                item_name = cells[1].text.strip() # отримання назви предмету з комірки 1 рядка
                grade = cells[1].text.strip() # отримання оцінки з комірки 1 рядка
                if item_name == "-":# якщо назва предмету "-" (пуста комірка)
                    grade = ""# то оцінка не зберігається
                grades.append(grade)# зберігання отриманої оцінки в список оцінок


        messagebox.showinfo(title='Успішно', message='Парсинг оцінок завершено!')
        cell_range = f"{start_cell}:{end_cell}" # формування діапазону комірок для запису даних
        sheet.update(cell_range, [[grade] for grade in grades]) # формування діапазону комірок для запису даних
        driver.quit() # формування діапазону комірок для запису даних



    # DESIGN
    root = tk.Tk()
    root.geometry("500x380")


    root.title("Парсниг оцінок")
    font_style = ("Helvetica", 14)
    username_label = tk.Label(root, text="Логін:", font=font_style)
    username_label.pack()
    username_entry = tk.Entry(root, font=font_style)
    username_entry.pack()
    password_label = tk.Label(root, text="Пароль:", font=font_style)
    password_label.pack()
    password_entry = tk.Entry(root, show="*", font=font_style)
    password_entry.pack()
    link_label = tk.Label(root, text="Посилання на преддмет:", font=font_style)
    link_label.pack()
    link_entry = tk.Entry(root, font=font_style)
    link_entry.pack()
    # викликаємо метод, для введення у форму
    load_credentials() 



    start_cell_label = tk.Label(root, text="Введіть початкову колонку (наприклад H7):", font=font_style)
    start_cell_label.pack()
    start_cell_entry = tk.Entry(root, font=font_style)
    start_cell_entry.pack()

    end_cell_label = tk.Label(root, text="Введіть кінцеву колонку (наприклад H50):", font=font_style)
    end_cell_label.pack()
    end_cell_entry = tk.Entry(root, font=font_style)
    end_cell_entry.pack()

    # введення за користувача 
    start_cell_entry.insert(0, "H3")
    end_cell_entry.insert(0, "H50") 




    login_button = tk.Button(root, text="Розпочати", font=font_style, command=parser_grade, bd=2, relief=tk.SOLID, highlightthickness=0, bg="#3F3F3F", fg="white", activebackground="#5F5F5F", activeforeground="white")
    login_button.pack(pady=10)



    root.mainloop()
except Exception as e:
    messagebox.showerror(title='Сталася помилка', message=f'{e}\n\nПомоліться... може щось зміниться')
    print(e)