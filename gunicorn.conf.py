# gunicorn.conf.py
workers = 4  # Number of worker processes
worker_class = 'uvicorn.workers.UvicornWorker'  # Use UvicornWorker
bind = '0.0.0.0:8000'  # Bind to port 8000
loglevel = 'info'  # Logging level
