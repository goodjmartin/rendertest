FROM ubuntu
RUN apt-get update
RUN yes | apt-get install python
RUN mkdir hello
WORKDIR /
ADD app.py / 
#CMD [ "ls"]
CMD [ "python","app.py"]
