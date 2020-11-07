FROM python:alpine3.7
COPY ./divtastic/ /app
WORKDIR /app
run pip3 install django
EXPOSE 8080
ENTRYPOINT [ "python" ]
CMD [ "python3 manage.py 0.0.0.0:8080"  ]