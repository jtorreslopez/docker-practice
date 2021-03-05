FROM ubuntu
COPY . /
RUN apt update && apt install -y python3 python3-dev python3-venv python3-pip
RUN pip3 install -r requirements.txt
ENTRYPOINT [ "python3" ]
CMD [ "app/main.py" ]
