FROM python
EXPOSE 5000
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD [“uvcorn”, “app.main:app”, “--host”, “0.0.0.0”]