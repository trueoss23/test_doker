FROM python

RUN pip install fastapi uvicorn

WORKDIR /app

COPY /app_1 .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "5000"]
