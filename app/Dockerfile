# pull official base image
FROM python:3.8

# set work directory
WORKDIR /longtran/blog_person

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# copy project
COPY . .

EXPOSE 8000


ENTRYPOINT ["python", "./manage.py"]
CMD ["runserver", "0.0.0.0:8000"]