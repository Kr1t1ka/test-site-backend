FROM python:3.9.2-alpine3.12

RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev libffi-dev

ADD . /app
WORKDIR /app

RUN apk add --no-cache jpeg-dev zlib-dev
RUN apk add --no-cache --virtual .build-deps build-base linux-headers \
    && pip install Pillow

RUN pip install -r requirements.txt

RUN ls

RUN chmod +x /app/start.sh

CMD ["./start.sh"]
