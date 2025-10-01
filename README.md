# Zomato Cloud Mediation API

## Deployment (Render)

1. Push repo to GitHub
2. Go to Render → New → Web Service
3. Connect repo
4. Build command: `pip install -r api/requirements.txt`
5. Start command: `uvicorn api.app:app --host 0.0.0.0 --port $PORT`
6. After deployment, copy the URL to `benchmark/benchmark.py` API_URL

## Benchmark

Run benchmark:
```bash
cd benchmark
python benchmark.py
