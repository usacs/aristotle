FROM python:latest
COPY $PROJECT_ROOT .
RUN pip install .
CMD ["python", "-m", "unittest"]
