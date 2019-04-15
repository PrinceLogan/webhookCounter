FROM python:3.6
ENV PYTHONUNBUFFERED 1
ENV C_FORCE_ROOT true
RUN mkdir /webhooksExplorer
RUN mkdir /static
RUN mkdir /config
ADD /config/requirements.pip /config/
WORKDIR /webhooksExplorer
ADD ./webhooksExplorer /webhooksExplorer
RUN pip install --upgrade pip
RUN pip install -r /config/requirements.pip
CMD python manage.py collectstatic --no-input;python manage.py migrate; gunicorn webhooksExplorer.wsgi -b 0.0.0.0:8000; while true; do python webhookProcessor.py ;sleep 5; done
