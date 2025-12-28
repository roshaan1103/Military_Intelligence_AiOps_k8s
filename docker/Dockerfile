FROM python:3.11-slim

WORKDIR /app

# Copy requirements.txt first and install dependencies
#COPY requirements.txt .
RUN pip install fastapi uvicorn joblib pandas scikit-learn

# Copy the rest of the app
COPY app/ .

# Ensure a dummy model.pkl exists to avoid runtime crash
RUN python -c "from sklearn.linear_model import LinearRegression; import joblib; joblib.dump(LinearRegression(), 'model.pkl')"

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

