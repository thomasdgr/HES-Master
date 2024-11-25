FROM python:3.8

WORKDIR /app

RUN pip install --upgrade pip
RUN pip install pdm

COPY . .

RUN pdm install

EXPOSE 5000
ENV FLASK_RUN_HOST 0.0.0.0
ENV FLASK_RUN_PORT 5000

CMD ["pdm", "run", "flask"]