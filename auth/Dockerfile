FROM python:3.6

WORKDIR /app

RUN apt-get -y update
RUN apt-get install -y python python-pip python-dev
RUN pip install pipenv
COPY Pipfile /app/
COPY Pipfile.lock /app/
RUN pipenv install --system --deploy --ignore-pipfile
COPY . /app
RUN python manage.py migrate
CMD ["python", "manage.py", "runserver", "0.0.0.0:80"]
EXPOSE 80