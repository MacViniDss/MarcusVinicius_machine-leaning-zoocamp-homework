
FROM agrigorev/zoomcamp-model:2025
WORKDIR /code
COPY pyproject.toml .


RUN pip install uv 
RUN uv pip install --system scikit-learn==1.6.1 fastapi uvicorn

COPY app.py .

COPY pipeline_v1.bin .

EXPOSE 9696
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "9696"]
