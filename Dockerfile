FROM daocloud.io/python:3-onbuild
ENV TZ=Asia/Shanghai
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
COPY . ./
RUN mv /etc/apt/sources.list /etc/apt/sources.list.bak && mv sources.list /etc/apt/
RUN apt-get update 
RUN apt-get install -y xdg-utils
#RUN apt-get install python3-pip /y
RUN pip3 install -r ./requirements.txt
#CMD ["python3","./run.py"]

