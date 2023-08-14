FROM python:latest

RUN apt update && apt install nginx -y
RUN apt-get update && apt-get install gunicorn -y
COPY ./nginx/default.conf  /etc/nginx/conf.d/default.conf

WORKDIR /app

COPY . .

RUN pip3 install -r requirements.txt
RUN chmod +x ./entrypoint.sh
EXPOSE 8000

CMD ["./entrypoint.sh"]
