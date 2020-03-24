FROM python:3.8.2-slim-buster

COPY .streamlit ~/
COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install -q -r requirements.txt

COPY . ./

CMD ["streamlit", "run", "app.py"]
