FROM python:3

COPY requirements.txt .
RUN pip install -r requirements.txt 
ADD mainapp.py /app/
WORKDIR /app
EXPOSE 5000
CMD [ "python", "./mainapp.py" ]
