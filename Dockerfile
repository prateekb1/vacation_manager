FROM python:3.8

ENV PYTHONUNBUFFERED 1

RUN mkdir /code

WORKDIR /code

COPY requirements.txt /code/

RUN pip install -r requirements.txt

COPY . /code/

# # Expose port 8000
# EXPOSE 8000

# # Start the Django development server
# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]