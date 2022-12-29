FROM python:3.8

WORKDIR /charts
COPY requirements.txt /chart/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /chart/requirements.txt

COPY . /charts 

CMD bash -c "while true; do sleep 1; done"
