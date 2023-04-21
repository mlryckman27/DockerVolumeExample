FROM python:3.10-alpine
WORKDIR /app
RUN apk add --no-cache gcc musl-dev linux-headers
COPY . .
CMD ["python", "app.py"]