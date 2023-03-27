# parser_grade
Прасинг оцінок з Мудла, у гугл таблицю на основі API ключа Google Cloud

!!! Використовується СhromeDriver !!!

Данна программа є "милицею". 
Можна викорастти API https://moodledev.io/docs/apis 
(але якщо у нас немає доступу до таблиці з оцінками на сайт Мудла) 
Доведеться використовувати бібліотеки selenium BeautifulSoup для парсингу з сайту (тобто брати елементи з сайту).

Для початку нам потрібно встановити потрібну версію chromedriver
https://chromedriver.chromium.org/downloads (щоб дізнатися власну версію, потрібно зайти chrome://settings/help (в налаштування Google Chroome)

![image](https://user-images.githubusercontent.com/92741398/227964591-03ce93c1-3c8e-4be7-b44c-b41584375b34.png)

У мене 111.0.5563.111 (останні три цифри не важливі, вже на сайті можемо знайти версію 111.0.5563)

Після встановлення пакету .zip, вам потрібно архівувати файл chromedriver.exe у будь-яку папку та зпустити (потім можете закрити).



Після цього переходимо до створення API (для запису у таблицю)
https://console.cloud.google.com/ Та створюємо новий проект.

Після цього переходимо на: 
![Screenshot_19](https://user-images.githubusercontent.com/92741398/227966807-3e01ba83-68fb-451b-8b61-86e5e639bcaa.png)

Обираємо наш проект
![Screenshot_20](https://user-images.githubusercontent.com/92741398/227967175-63692cf9-202f-4834-8d8e-f20fc73d29a6.png)

Шукаємо google sheets api

![Screenshot_23](https://user-images.githubusercontent.com/92741398/227967784-705e7410-084e-4632-a1fd-0987b6af5bdd.png)

Та активуємо API
![Screenshot_24](https://user-images.githubusercontent.com/92741398/227967898-2a05b7e6-5d78-45ee-b757-b2ab8db067b6.png)

Перехід на Credentials
![Screenshot_30](https://user-images.githubusercontent.com/92741398/227970259-b2d40073-9562-43ab-8341-9dc818207295.png)
В нас вже є пошта, яку ми можемо додати у нашу таблицю
![Screenshot_31](https://user-images.githubusercontent.com/92741398/227970264-67c3b7b0-74f1-4c73-91d0-060366c2eb18.png)

Копіюємо її, та вставляємо (важливо щоб був редактор)
![Screenshot_32](https://user-images.githubusercontent.com/92741398/227970979-9fdb00c9-c4ef-468b-9cdc-45faaaaba31d.png)
![Screenshot_33](https://user-images.githubusercontent.com/92741398/227970984-3e69b4bd-517b-4cfa-890c-acfebafc73db.png)


Далі виконуємо прості кроки для отримання credentials.json сервісний файла 
(для авторизації користувача та доступ до гугл-таблиці)

![Screenshot_40](https://user-images.githubusercontent.com/92741398/227973026-596117a9-42fc-4651-9f1f-b3c08c15e507.png)
![Screenshot_41](https://user-images.githubusercontent.com/92741398/227973032-f7f51852-b09b-4b46-b817-9f175745f038.png)
![Screenshot_42](https://user-images.githubusercontent.com/92741398/227973037-bc9410e0-1a57-4891-b17c-9995523d9163.png)
![Screenshot_43](https://user-images.githubusercontent.com/92741398/227973041-26abc450-7577-45bb-b227-e3d8f93c8882.png)


Далі перекідаємо файл у нашу папку з Хром Драйвером, далі 
!!! переменовуємо у credentials2.json !!!
![image](https://user-images.githubusercontent.com/92741398/227973392-848c8de3-0266-4855-b44b-af69ffe4f7ac.png)

Далі створюємо у ції папці файли:
sheet_id.txt (у якій буде міститися айді таблиці
https://docs.google.com/spreadsheets/d/   після d/   1ZKJwqgzrZ6Wux0tbwW5e0v7m6g1o0KiFjqV0FPP2WtU  до /edit#gid=458659454)

У credentials.txt
![image](https://user-images.githubusercontent.com/92741398/227974094-c6afa03a-aa31-4472-aa81-59d63d1ba193.png)

Ці файли потрібно щоб кожного разу не вводити дані у программу, та мати можливість записувати у інші таблиці чи використовувати інші аккаунти з доступом до оцінок.


Після цього завантажеємо наш файл .ЕХЕ у папку, та запускаємо.
У випадок, якщо стаенться помилка, повідомте мені :)
