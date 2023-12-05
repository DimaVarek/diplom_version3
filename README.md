# diplom_version3
Summary: <br>
This project is an application related to the diploma thesis titled "Exploring Machine Learning Methods in Predicting Match Outcomes in Professional Counter-Strike: Global Offensive Scene."

The diploma thesis focuses on comparing machine learning methods in a binary classification task using CS:GO match data.

Data Collection: <br>
The entire project, except for the "research" folder, is responsible for data collection and initial processing. The "parsing" folder handles data parsing from the hltv.org website. In the "preprocessing" folder, match data is transformed from JSON files to CSV tables for further model training. Everything is initiated from the "main.py" file.

Method Comparison: <br>
The "research" folder is responsible for comparing methods. It contains data and three folders, each dedicated to a table derived from the data. More details about the methods used and the entire thesis can be found in the actual diploma thesis.

Results: <br>
64% accuracy. Probabilistic models were not considered, although now, in retrospect, it seems like the most reasonable idea. Perhaps, at some point in the future, I will explore this avenue.

Общее:<br>
Данный проект является приложением к дипломной работе по теме: Исследование методов 
машинного обучения в задаче предсказания результатов матчей на профессиональной 
сцене в Counter-Strike: Global Offensive

Дипломная работа посвящена сравнению методов машинного обучения в задаче бинарной классификации на примере матчей в кс:го.

Сбор данных:<br>
За сбор и первичную обработку данных отвечает весть проект, кроме папки research.
В папке parsing все, что отвечает за парсинг данных с сайта hltv.org.
В папке preprocessing все, что отвечает за преобразования мачей из json файлов в csv таблицы, для дальнейшего обучения на них моделей.
Все запускается из файла main.py.

Сравнение методов:<br>
За сравнения методов отвечает папка reseach. В ней находятся данные и 3 папки, каждая из которых посвящена своей таблице, полученной из данных.
Подробнее про сами используемые методы и весь диплом можно прочитать в самой дипломной работе.

Результаты:<br>
64% accuracy. 
Я не рассмотривал вероятностные модели, хотя сейчас, после всего, это кажется самой разумной идеей. Быть может когда-нибудь рассмотрю. 
