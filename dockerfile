FROM python:3.7.3

WORKDIR /app/

COPY api/api.py requirements.txt /app/

RUN pip install -r requirements.txt && chmod +x api.py

ENTRYPOINT ./api.py

# Run the app.  CMD is required to run on Heroku
# $PORT is set by Heroku			
CMD gunicorn --bind 0.0.0.0:$PORT wsgi