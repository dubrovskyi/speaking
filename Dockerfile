FROM python:3

WORKDIR /usr/app/speaking/

COPY . .

#ENV FLASK_RUN_HOST 0.0.0.0
#RUN apk add --no-cache gcc musl-dev linux-headers

RUN pip3 install -r requirements.txt

CMD ["python3", "runner.py"]
