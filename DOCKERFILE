FROM python:3.13

WORKDIR /src

COPY src/requirements.txt .

RUN pip install -r requirements.txt

COPY src/ .

CMD ["python", "./main.py"]
