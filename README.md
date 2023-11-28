# app-api

### To run this program:

Create venv: python3 -m venv "your venv name (.venv or venv, etc)"</br>
Activate your venv: source "venv-name"/bin/activate</br>
Check your venv: which python</br>
Pip install: pip install -r requirements.txt</br>
Run: uvicorn main:app --reload</br>
</br>

### To run pytest:
Do: python -m pytest in your terminal
</br>

### Docker:
Navigate to the root of this repo.
</br>
* Build the image: docker build -t opp_app .
* Run the container: docker run -d --name opp_app_V1 -p 8000:8000 opp_app
* Stop the container: docker stop opp_app_V1
* Remove the container: docker remove opp_app_V1
