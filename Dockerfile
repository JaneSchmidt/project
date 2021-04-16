FROM ubuntu:18.04

#RUN git clone https://github.com/tbalson/cpu_test.git

WORKDIR predict_demo/
COPY . /predict_demo

#RUN git pull

EXPOSE 8080

RUN pip install -r requirements.txt

#CMD ["make", "start"]
