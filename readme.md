# Mellows

Find match music for your script!

Mellows will allow you to find music in our database that suit the emotion of your script. By using [synesketch](http://krcadinac.com/synesketch/) , your search will get nearly perfect accuracy. Don't wait for long time, just clone and start it.

### Language ###
- Python 3.4
- Java 8 :JDK and JRE
- HTML, CSS, JS

### Framework ###
- Django

### Python Library ###
- [Pyjnius](https://github.com/kivy/pyjnius)

#### How it works [ubuntu] ###
1. clone [this repository](https://github.com/ryorda/MusicScriptPrediction.git)
2. install [JDK 1.8](http://www.webupd8.org/2012/09/install-oracle-java-8-in-ubuntu-via-ppa.html)
3. install Pyjnius. read [docs](https://pyjnius.readthedocs.io/en/latest/installation.html). note that `make` command is optional, it may produce errors
4. try your pyjnius `python3 test.py` 
5. install django using pip3 ( pip if your default python version is 3.X ). read [docs](https://www.djangoproject.com/download/)
6. change cwd to Application. type `python3 manage.py runserver` (make sure the predictlib.jar is generated)
7. open browser and type `http://localhost:8000/app`
8. try to submit some script
9. If you found error, it because your EmotionSong DB hasn't configured. Hence, access this url `http://localhost/app/api/recomputeall?username=<username>&password=<password>` to initialize EmotionSong




### Important!!! ###
- find `Application/mainapp/views.py` , replace `JAVA_HOME` if you're not in ubuntu or found error with key `JAVA_HOME`

##### How to generate predictlib #####
1. open eclipse
2. import `General > Existing Projects into Workspace`, select the Synesketch folder
3. export Synesketch as `Java > Runnable JAR File`
4. export destination to Application/predictlib.jar , choose library handling option `Copy required libraries into a subfolder ...`
5. click finish