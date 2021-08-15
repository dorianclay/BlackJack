FROM python:3.9
WORKDIR /app
COPY requirements.txt /app/
RUN pip3 install -r requirements.txt
COPY /library /app/library
COPY /server /app/server
COPY /src /app/src
COPY gun.py /app/
COPY run_server.sh /app/
EXPOSE 5000
CMD ["bash", "run_server.sh"]
