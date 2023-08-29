FROM python:alpine


WORKDIR /app
COPY . /app/
COPY requirements.txt /tmp/

RUN pip install --requirement /tmp/requirements.txt




# RUN python3 -m pip install --user  /app/book_auth




EXPOSE 8001