FROM python:3

WORKDIR /var/www/html

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["gunicorn", "--graceful-timeout", "5", "main:app",  "-w", "4", "-b", "0.0.0.0:8080"]
