FROM python

RUN pip install fastapi uvicorn pymongo

WORKDIR ./app

COPY . .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
