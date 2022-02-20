# medical_imaging_miniproject

Background: 
- Transfer-learning based models used in tumour classification
- Inception v3 is a transfer-learning model - deep learning based on CNNs, used for image classification

Plan:
- Run Inception v3 (pretrained on ImageNet) on cancer histology images & look at performance - Google tutorials suggest 2000 images in examples for reasonable runtime (will use Google CoLab) (https://colab.research.google.com/github/google/eng-edu/blob/master/ml/pc/exercises/image_classification_part3.ipynb#scrollTo=dI5rmt4UBwXs). This has been done before in other studies for tumour classification. 
- Would use subset of P-CAM dataset https://github.com/basveeling/pcam - binary classification, metastatic tissue present = 1 (kaggle version https://www.kaggle.com/c/histopathologic-cancer-detection/data)
- If time, will use LIME for explainability (lime python package available) - why/how did model classify these images? XAI needed for trust in clinical applications. ipynb tutorials available in github for package (https://github.com/marcotcr/lime/blob/master/doc/notebooks/Tutorial%20-%20images.ipynb) which shows how to use.