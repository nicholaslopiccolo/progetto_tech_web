# Progetto Tecnologie Web 2022
Il seguente progetto è stato sviluppato nel linguaggio python con l'utilizzo del framework web [django](https://docs.djangoproject.com/en/4.1/).
## Librerie aggiuntive
Per lo sviluppo delle features ho adottato l'utilizzo di diverse librerie:
- django-ajax-datatable è una libreria che permette la facile creazione di datables per permettere agli utenti di visionare facilmente i dati nell'applicazione
- django-widget-tweaks concede l'utilizzo di features nei templates in jinja come il rendering delle field dei form e permette di aggiungere classi o tag specifici
- Pillow modulo che permette l'inserimento di immagini nei modelli django
- python-decouple libreria che permette di recuperare dati dalle variabili d'ambiente nei file .env

## Installazione
Prima di tutto bisogna clonare il repository git e spostarci al suo interno:
```
git clone https://github.com/nicholaslopiccolo/progetto_tech_web.git
cd progetto_tech_web
```
Per un installazione ottimale di consiglia l'utilizzo di un environment virtuale con uno dei due moduli seguenti:
- virtualenv
```
pip install virtualenv
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
```
- pipenv
```
pip install pipenv
pipenv shell
pip install -r requirements.txt
```

Per completare l'installazione bisogna eveguire la migrazione delle modifiche con il seguente comando:
```
python .\manage.py migrate
```
Per eseguire il programma:
```
python .\manage.py runserver
```

Per creare un utente admin lanciare il seguente comando e seguire la procedura
```
python manage.py createsuperuser
```
