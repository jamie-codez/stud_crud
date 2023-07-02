FROM python:3.9
LABEL authors="jamie"
ENV WORKDIRECTORY /app

WORKDIR $WORKDIRECTORY
COPY requirements.txt .
RUN pip3 install -r requirements.txt

COPY . $WORKDIRECTORY
ADD .env $WORKDIRECTORY

EXPOSE 8000

#RUN export PYTHONPATH=$PWD

CMD ["python3","app/main.py"]