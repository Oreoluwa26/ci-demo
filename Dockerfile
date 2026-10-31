FROM python:3.12-slim

WORKDIR /app

COPY dist/*.whl .
RUN pip install --no-cache-dir *.whl

EXPOSE 5000

CMD ["flask", "--app", "ciapp.app", "run", "--host", "0.0.0.0"]
