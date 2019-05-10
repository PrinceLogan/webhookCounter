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
RUN apt-get update
RUN apt-get install -y nginx
RUN apt-get clean
RUN rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
RUN echo "daemon off;" >> /etc/nginx/nginx.conf
ADD /config/nginx/mydjango.conf /etc/nginx/sites-available/mydjango
RUN ln -s /etc/nginx/sites-available/mydjango /etc/nginx/sites-enabled
EXPOSE 8000
CMD python manage.py collectstatic --no-input;python manage.py migrate; gunicorn --daemon --workers 3 --bind unix:/webhooksExplorer/webhooksExplorer.sock webhooksExplorer.wsgi;sleep 5; nginx
