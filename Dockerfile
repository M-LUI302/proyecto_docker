FROM python:3 
MAINTAINER lupitaOxff <root@lupita0xff.me>
ENV PYTHONUNBUFFERED 1
RUN mkdir -p /opt/services/flaskapp/src
COPY requirements.txt /opt/services/flaskapp/src
WORKDIR /opt/services/flaskapp/src
RUN pip install -r requirements.txt
COPY . /opt/services/flaskapp/src
EXPOSE 6565
CMD ["python", "Acciones.py"]
