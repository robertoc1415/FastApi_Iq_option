FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7
COPY ./app /app
WORKDIR /app
RUN python -m pip install --upgrade pip
RUN apt install vim -y
RUN git clone https://github.com/robertoc1415/iqoptionapi-master2.git
WORKDIR /app/iqoptionapi-master2/iqoptionapi-master
RUN pip install -r requirements.txt
RUN python setup.py install
WORKDIR /home
RUN apt-get update && apt-get install -y \
  wget \
  build-essential \
  automake \
  pkg-config \
  libtool \
  python3-dev \
  python3-setuptools

RUN wget http://prdownloads.sourceforge.net/ta-lib/ta-lib-0.4.0-src.tar.gz && \
  tar -xvzf ta-lib-0.4.0-src.tar.gz && \
  cd ta-lib/ && \
  ./configure --prefix=/usr && \
  make && \
  make install

RUN python3 -m pip install ta-lib
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
# CMD ["bash"]


# FROM python:3.9
# RUN pip install fastapi uvicorn pydantic
# # Copy your application code to the container
# COPY . /app

# # Set the working directory to /app
# WORKDIR /app
# # Install dependencies
# # RUN python -m pip install -r requirements.txt

# # Run the application
# CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]

# FROM python:3.9

# # Instalamos las dependencias necesarias para nuestra aplicación
# COPY requirements.txt .
# RUN pip install -r requirements.txt

# # Copiamos nuestro código a la imagen
# COPY . .

# # Exponemos el puerto en el que queremos que nuestra aplicación FastAPI escuche
# EXPOSE 80

# # Establecemos la entrada a nuestro contenedor
# ENTRYPOINT ["python"]

# # Especificamos el archivo principal de nuestra aplicación
# CMD ["main.py"]



# FROM tiangolo/uvicorn-gunicorn-fastapi:latest
# # CMD [ "bash" ]
# # FROM python:3.9

# # COPY . /archivos/app2
# WORKDIR /home
# RUN apt-get update && apt-get install -y \
#   wget \
#   build-essential \
#   automake \
#   pkg-config \
#   libtool \
#   python3-dev \
#   python3-setuptools

# RUN wget http://prdownloads.sourceforge.net/ta-lib/ta-lib-0.4.0-src.tar.gz && \
#   tar -xvzf ta-lib-0.4.0-src.tar.gz && \
#   cd ta-lib/ && \
#   ./configure --prefix=/usr && \
#   make && \
#   make install

# RUN python3 -m pip install ta-lib


# RUN git clone https://github.com/robertoc1415/iqoptionapi-master2.git
# # WORKDIR /usr/src/trabajo/iqoptionapi-master2/iqoptionapi-master
# WORKDIR /app/iqoptionapi-master2/iqoptionapi-master

# RUN python -m pip install --upgrade pip
# RUN python setup.py install
# RUN pip install -r requirements.txt
# CMD [ "bash" ]












# FROM tiangolo/uvicorn-gunicorn-fastapi:latest
# FROM api:5.0
# COPY requirements.txt /tmp/requirements.txt
# RUN pip install --no-cache-dir -r /tmp/requirements.txt
# COPY . /app2
# WORKDIR /app2
# CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]



# FROM python:3.9
# # TA-Lib
# RUN apt-get update && apt-get install -y \
#   wget \
#   build-essential \
#   automake \
#   pkg-config \
#   libtool \
#   python3-dev \
#   python3-setuptools

# RUN wget http://prdownloads.sourceforge.net/ta-lib/ta-lib-0.4.0-src.tar.gz && \
#   tar -xvzf ta-lib-0.4.0-src.tar.gz && \
#   cd ta-lib/ && \
#   ./configure --prefix=/usr && \
#   make && \
#   sudo make install
# RUN git clone https://github.com/mrjbq7/ta-lib.git /ta-lib-py && cd ta-lib-py && python setup.py install
# WORKDIR /usr/src/trabajo
# RUN git clone https://github.com/robertoc1415/iqoptionapi-master2.git
# WORKDIR /usr/src/trabajo/iqoptionapi-master2/iqoptionapi-master

# # COPY [".", "/usr/src/"]
# # WORKDIR /usr/src/iqoptionapi-master
# RUN python -m pip install --upgrade pip
# RUN python setup.py install
# RUN pip install -r requirements.txt


# FROM tiangolo/uvicorn-gunicorn:python3.9
# # FROM tiangolo/uvicorn-gunicorn-fastapi:latest
# # FROM python:3.9

# RUN apt-get update && apt-get install -y \
#   wget \
#   build-essential \
#   automake \
#   pkg-config \
#   libtool \
#   python3-dev \
#   python3-setuptools \
#   git

# RUN wget http://prdownloads.sourceforge.net/ta-lib/ta-lib-0.4.0-src.tar.gz && \
#   tar -xvzf ta-lib-0.4.0-src.tar.gz && \
#   cd ta-lib/ && \
#   ./configure --prefix=/usr && \
#   make && \
#   make install

# RUN python3 -m pip install ta-lib


# COPY requirements.txt /tmp/requirements.txt
# RUN pip install --no-cache-dir -r /tmp/requirements.txt


# RUN git clone https://github.com/robertoc1415/iqoptionapi-master2.git
# WORKDIR /usr/src/trabajo/iqoptionapi-master2/iqoptionapi-master

# # COPY [".", "/usr/src/"]
# # WORKDIR /usr/src/iqoptionapi-master
# RUN python -m pip install --upgrade pip
# RUN python setup.py install
# RUN pip install -r requirements.txt