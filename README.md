# Проект по автоматизации тестовых сценариев для сайта компании T1
## <img width="40" height="40" style="vertical-align:middle" title="Folder" src="media/images/yellow-computer-folder.png"> Содержание:

- <a href="#stech">Используемый стек технологий и инструментов</a>
- <a href="#check">Реализованные проверки</a>
- <a href="#engine">Запуск автотестов</a>
- <a href="#build">Сборка в Jenkins</a>
- <a href="#report">Интеграция с Allure</a>
- <a href="#testops">Интеграция с Allure TestOps</a>
- <a href="#jira">Интеграция с Jira</a>
- <a href="#telegram">Уведомления в Telegram через бота</a>
- <a href="#video">Видео отчет запуска тестов (Selenoid)</a>

<a id="stech"></a>
## <img width="40" height="40" style="vertical-align:middle" title="Folder" src="media/images/programm.jpg"> Используемый стек технологий и инструментов

| Python                                                    | Pycharm                                                    | GitHub                                                    | Pytest                                                    | Selenide                                                    | Selen                                                      | Allure<br/>Report                                                | Allure <br> TestOps                                               | Jenkins                                                    | Jira                                                    |                                                    Telegram |
|:----------------------------------------------------------|------------------------------------------------------------|-----------------------------------------------------------|-----------------------------------------------------------|-------------------------------------------------------------|------------------------------------------------------------|------------------------------------------------------------------|-------------------------------------------------------------------|------------------------------------------------------------|---------------------------------------------------------|------------------------------------------------------------:|
| <img height="50" src="media/logo/Python.png" width="50"/> | <img height="50" src="media/logo/Pycharm.png" width="50"/> | <img height="50" src="media/logo/GitHub.svg" width="50"/> | <img height="50" src="media/logo/Pytest.png" width="50"/> | <img height="50" src="media/logo/Selenide.png" width="50"/> | <img height="50" src="media/logo/Selene.png" width="50"/>  | <img height="50" src="media/logo/Allure_Report.svg" width="50"/> | <img height="50" src="media\logo\Allure_TestOps.svg" width="50"/> | <img height="50" src="media/logo/Jenkins.svg" width="50"/> | <img height="50" src="media/logo/Jira.svg" width="50"/> | <img height="50" src="media\logo\Telegram.svg" width="50"/> |


<a id="chek"></a> 
##  <img width="40" height="40" style="vertical-align:middle" title="List" src="media/images/todo.png"> Реализованные проверки
- Проверка открытия нужного сайта
- Проверка контента хедера
- Проверка поиска
- Проверка обратной связи
- Проверка информации о холдинге
- Проверка информации о пресс-центре

<a id="engine"></a> 
## <img width="40" height="40" style="vertical-align:middle" title="Play" src="media/images/play.jpg"> Запуск автотестов


### Запуск тестов из терминала удаленно (Selenoid): 
```
SELENOID_LOGIN=user1
SELENOID_PASS=1234
SELENOID_URL=selenoid.autotests.cloud      
```
### Запуск тестов c задаными параметрами в Jenkins:   
```   
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pytest .
```
<a id="build"></a> 
## <img width="40" height="40" style="vertical-align:middle" title="Jenkins" src="media/logo/Jenkins.svg"> Сборка в Jenkins

Для запуска сборки необходимо перейти в раздел **"Build with Parameters"** и нажать кнопку **"Build"**.
<p align="center">
<img title="Jenkins Build" src="media/screenshots/JenkinsBuild.png"> 
</p>

После выполнения сборки, в блоке **Build History** напротив номера сборки появятся значки <img src="media\logo\Allure_TestOps.svg" width="15" height="15">
и <img src="media\logo\Allure_Report.svg" width="15" height="15"> , при клике на которые откроются соответствующие
артефакты.  

## <img width="40" height="40" style="vertical-align:middle" title="Allure Report" src="media/logo/Allure_Report.svg"> Интеграция с Allure

<a id="report"></a> 
### Allure отчет

<p align="center">   
<img title="Jenkins Build" src="media/screenshots/Allure Report1.png">    
</p>

### Подробнее   
<p align="center">     
<img title="Jenkins Build" src="media/screenshots/Allure Report2.png">    
</p>       

## <img width="40" height="40" style="vertical-align:middle" title="Allure TestOps" src="media/logo/Allure_TestOps.svg"> Интеграция с Allure TestOps
          

<a id="testops"></a>
### Allure TestOps отчет

#### Overview

<p align="center">    
<img title="Allure TestOps Overview" src="media/screenshots/Allure_TestOps1.png">
</p>

#### DashBoards
<p align="center">
<img title="Allure TestOps DashBoards" src="media/screenshots/Allure_TestOps3.png">
</p>


#### Подробнее

<p align="center">
<img title="Test Results in Alure TestOps" src="media/screenshots/Allure_TestOps2.png">
</p>


<a id="jira"></a> 
## <img width="40" height="40" style="vertical-align:middle" title="Jira" src="media/logo/Jira.svg"> Интеграция с Jira


<p align="center">
<img title="Jira Task" src="media/screenshots/Jira.png">
</p>

## <img width="40" height="40" style="vertical-align:middle" title="Telegram" src="media/logo/Telegram.svg"> Уведомления в Telegram через бота


<a id="telegram"></a> 
<p align="center">
<img title="Telegram Notifications" src="media/screenshots/Notifications.png">
</p>


<a id="video"></a> 
## <img width="40" height="40" style="vertical-align:middle" title="Selenoid" src="media/logo/Selenoid.svg"> Видео отчет запуска тестов (Selenoid)

<p align="center">
  <img title="Selenoid Video" src="media/gifs/T1.gif">
</p>