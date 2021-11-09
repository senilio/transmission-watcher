FROM python:3
ADD watcher.py /
RUN pip install transmission_rpc
CMD ["python", "watcher.py"]
