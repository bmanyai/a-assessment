FROM python:3

RUN pip install jinja2 
ADD configure.py /app/
WORKDIR /app
CMD [ "python", "./configure.py" ]
