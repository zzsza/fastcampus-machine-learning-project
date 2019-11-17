### Taxi Demand Prediction
- Python 3.7 사용
- Structure

    ```
    ├── README.md
    ├── base_data.py
    ├── config.yaml
    ├── your_key.json
    ├── main.py
    ├── models
    │   └── rf_model
    ├── requirements.txt
    ├── rf_trainer.py
    └── utils.py
    ```

---

### Environment
- Python 가상 환경

    ```
    virtualenv env
    source env/bin/activate
    pip3 install -r requirements.txt
    ```

- config.yaml의 project, jwt 수정
- 이 폴더에 Google Cloud Platform keyfile 다운로드

---

### Local
- Train

    ```
    python3 main.py --dev_env production --mode train
    ```
    
- Predict

    ```
    python3 main.py --dev_env production --mode predict
    ```
    
---
    
### Production
- Train

    ```
    python3 main.py --dev_env production --mode train
    ```
    
- Predict

    ```
    python3 main.py --dev_env production --mode predict
    ```
    
### 