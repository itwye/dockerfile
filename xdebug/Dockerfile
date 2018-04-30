
FROM python:2.7.14
MAINTAINER itwye<itwye@qq.com>

RUN apt-get update && \
    apt-get install -y python-dev && \
    pip install bottle && \
    pip install psutil && \
    apt-get remove -y python-dev && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  

COPY xdebug.py  /

CMD /usr/local/bin/python /xdebug.py