# Use a imagem base Python
FROM python:3


RUN pip install Django==4.0
#RUN apt install python-pip -y
RUN pip install mysqlclient
RUN pip install cx-oracle

COPY templates/technical_404.html ./usr/local/lib/python3.12/site-packages/django/views/templates/
COPY templates/technical_500.html ./usr/local/lib/python3.12/site-packages/django/views/templates/

WORKDIR /opt/oracle

RUN apt-get update && apt-get install -y libaio1 libpq-dev wget unzip && rm -rf /var/lib/apt/lists/*
RUN wget https://download.oracle.com/otn_software/linux/instantclient/instantclient-basiclite-linuxx64.zip && \
    unzip instantclient-basiclite-linuxx64.zip && rm -f instantclient-basiclite-linuxx64.zip && \
    cd /opt/oracle/instantclient* && rm -f *jdbc* *occi* *mysql* *README *jar uidrvci genezi adrci && \
    echo /opt/oracle/instantclient* > /etc/ld.so.conf.d/oracle-instantclient.conf && ldconfig    

# Define o diretório de trabalho no contêiner
WORKDIR /sentinela/

COPY . ./
# Copia os arquivos do aplicativo para o contêiner
EXPOSE 8003
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
CMD python3 manage.py runserver 0.0.0.0:8003
