FROM python:latest

RUN apt update && apt install nginx -y


WORKDIR /app

COPY . .

RUN pip3 install -r requirements.txt
RUN chmod +x ./entrypoint.sh
EXPOSE 8000

CMD ["./entrypoint.sh"]
