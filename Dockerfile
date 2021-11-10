FROM python:3
ENV PYTHONUNBUFFERED=1
ADD watcher.py /
RUN pip install transmission_rpc
CMD ["python", "watcher.py"]
