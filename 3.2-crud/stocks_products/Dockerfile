FROM python:3.10-alpine

WORKDIR /usr/src/api


RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev

RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

RUN mkdir $WORKDIR/staticfiles

COPY ./entrypoint.sh .
RUN sed -i 's/\r$//g' /usr/src/api/entrypoint.sh
RUN chmod +x /usr/src/api/entrypoint.sh

# copy project
COPY . .

# run entrypoint.sh
ENTRYPOINT ["/usr/src/api/entrypoint.sh"]