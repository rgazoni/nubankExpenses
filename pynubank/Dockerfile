FROM python:bullseye

RUN apt-get update
RUN pip install mysql-connector-python
RUN pip install pynubank

WORKDIR /app

ENTRYPOINT [ "/bin/bash" ]
