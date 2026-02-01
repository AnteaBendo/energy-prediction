FROM python:3.11-slim

RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir \
    tensorflow \
    matplotlib \
    scipy \
    numpy \
    statsmodels \
    scikit-learn \
    pandas \
    joblib

ADD ../../code/apply_ann_solution.py /codeBase/apply_ann_solution.py
ADD ../../code/apply_ols_solution.py /codeBase/apply_ols_solution.py