FROM ubuntu:16.04
FROM python:3
ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8

COPY cluster_test.py /root/
COPY requirements.txt /tmp/requirements.txt

# Provision container

#install required dependencies which are located at /tmp/requirements.txt in exe image
RUN pip install -r /tmp/requirements.txt

CMD python3 /root/cluster_test.py