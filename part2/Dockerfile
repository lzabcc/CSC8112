# Base on image_full_name (e.g., ubuntu:18.04) docker image
FROM python:3.8.12

# Switch to root
USER root

# Copy all sources files to workdir
ADD sub.py Docker_data/docker

# Change working dir
WORKDIR /home/student/Desktop/Docker_data/docker

COPY sub.py .
# Prepare project required running system environments
# requirements.txt is a document that pre-define any python dependencies with versions required of your code
RUN pip3 install datetime
RUN pip3 install paho-mqtt
RUN pip3 install requests
RUN pip3 install pika

# Start task
CMD python3 sub.py
