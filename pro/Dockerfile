FROM python:3.11

WORKDIR /pro

COPY requirements.txt .

RUN pip --no-cache-dir install -r requirements.txt

COPY . .

RUN python manage.py makemigrations
RUN python manage.py migrate

CMD ["python", "manage.py", "runserver", "0.0.0.0:80"]