<h2>Серверная часть веб-приложения для проведения теста, с не ограниченым количеством результатов.</h3>

<ul><h3>Технологии:</h3>
    <h5>
          <li>django</li>
          <li>DRF</li>
          <li>JWT</li>
    </h5>
	</ul>
<h5>
База: postgresql<br>
Хранилище: локальное, но можно подключить AWS S3

Запуск:<br>
-Локально:<br> Запусить файл start.sh
<p>
-В докере:<br>
# docker build . -t test:1<br>
# docker run test:1
</p>
</h5>

<ul><h3>Подключение к базе, через переменные в env </h3>
    <h5>
          <li>DB_NAME - имя базы</li>
          <li>DB_USER - имя пользователя </li>
          <li>DB_PASSWORD - пароль</li>
          <li>DB_HOST - адрес базы</li>
          <li>DB_PORT - порт</li>
    </h5>
	</ul>





