from fastapi import FastAPI, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware
from preprocess import parse_csv
from detectors import detect_zscore_anomalies, detect_isolationforest

app = FastAPI()
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])

@app.post("/analyze/")
async def analyze(file: UploadFile = File(...), method: str = Form("zscore"), column: str = Form("value")):
    content = await file.read()
    df = parse_csv(content)

    if method == "zscore":
        result_df = detect_zscore_anomalies(df, column)
    else:
        result_df = detect_isolationforest(df, [column])

    return result_df.to_dict(orient="records")
