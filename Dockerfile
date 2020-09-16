FROM python:3.7-slim

COPY requirements.txt /app/
RUN pip install --upgrade pip && pip install --no-cache-dir -Ur /app/requirements.txt

COPY . /app/
WORKDIR /app/

CMD /bin/bash