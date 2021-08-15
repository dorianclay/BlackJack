FROM python3.9
WORKDIR /app
COPY /library /app/
COPY /server /app/
COPY /src /app/
COPY requirements.txt /app/
COPY gun.py /app/
COPY run_server.sh /app/
RUN pip3 install -r requirements.txt
CMD ["bash", "run_server.sh"]
