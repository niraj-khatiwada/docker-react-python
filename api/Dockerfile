FROM python:3.10-alpine3.18

WORKDIR /usr/app/backend

COPY Pipfile Pipfile.lock ./

RUN pip install pipenv
RUN pipenv requirements > requirements.txt

RUN pip install -r requirements.txt

COPY . ./

CMD ["pipenv", "run", "server"]