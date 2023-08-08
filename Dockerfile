FROM python:3.10.12

ENV PYTHONPATH="${PYTHONPATH}:/app"

RUN mkdir /app
WORKDIR /app

COPY requirements.txt /app/requirements.txt
RUN pip install --upgrade pip \
    && pip install --no-cache-dir -r /app/requirements.txt

COPY . /app/

EXPOSE 5000

CMD [ "flask", "--app", "src.app", "run","--host","0.0.0.0","--port","5000"]