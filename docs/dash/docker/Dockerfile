FROM python:3.9
MAINTAINER MLEXCHANGE TEAM

RUN ls
COPY docker/requirements.txt requirements.txt

RUN apt-get update && apt-get install -y \
    build-essential \
    wget \
    python3-pip\
    ffmpeg\
    libsm6\
    libxext6 

RUN pip3 install --upgrade pip &&\
    pip3 install -r requirements.txt 

#EXPOSE 8000

WORKDIR /app/dash
ENV HOME /app/dash
COPY src src
ENV PYTHONUNBUFFERED=1

CMD ["bash"]
