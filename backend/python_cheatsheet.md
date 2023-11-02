Initialize an virtual environment: python3 -m vent .venv
Activate an VE: source .venv/bin/activate
Deactivate and VE: deactivate
Run app in Docker with automatic reloading and debug mode: 
Dockerfile
    FROM python
    EXPOSE 5000
    WORKDIR /app
    COPY requirements.txt
    RUN pip install -r requirements.txt
    COPY . .
    CMD [“uvcorn”, “app.main:app”, “--host”, “0.0.0.0”]

Build a docker image: docker build -t <app name> .
Run a docker image: docker run -dp 8005:8000 <app name>
Run docker image reload with code changes:  docker run -dp 8005:8000 -w /app -v $(pwd):/app <app name>
Access on 127.0.0.1:8005python