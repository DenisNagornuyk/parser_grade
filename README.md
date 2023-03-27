# parser_grade
Прасинг оцінок з Мудла, у гугл таблицю на основі API ключа Google Cloud

!!! Використовується СhromeDriver !!!

Данна программа є "милицею". 
Тут я використав бібліотеки selenium BeautifulSoup для парсингу з сайту (тобто брав елементи з сайту).

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
![image](https://user-images.githubusercontent.com/92741398/227967306-af4af0db-d990-4760-b9fd-48e3b2e3f4d8.png)

![Screenshot_22](https://user-images.githubusercontent.com/92741398/227967772-4e930523-4092-4087-84ea-a939866034ca.png)
![Screenshot_23](https://user-images.githubusercontent.com/92741398/227967784-705e7410-084e-4632-a1fd-0987b6af5bdd.png)

Та активуємо API
![Screenshot_24](https://user-images.githubusercontent.com/92741398/227967898-2a05b7e6-5d78-45ee-b757-b2ab8db067b6.png)



https://docs.google.com/spreadsheets/d/    1ZKJwqgzrZ6Wux0tbwW5e0v7m6g1o0KiFjqV0FPP2WtU   /edit#gid=458659454
