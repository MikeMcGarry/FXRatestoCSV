FROM python:3

WORKDIR /usr/src

ADD requirements.txt .

RUN pip install -r requirements.txt

CMD ["python", "tradermade.py"]