# ImageProcessingApplications
Simplistic UI to perform various image processing applications

## Note

Works only with python 3.7.6

## How to run


**1. Install Dependencies**
```
pip install -r requirements.txt
```

**2. Run Docker Image**
```
docker run -d -p 5000:5000 --gpus=all 
r8.im/microsoft/bringing-old-photos-back-to-life@sha256:4c6865805a5a9dd5962782ce2375424bf8b578fa297c00a4624041f34b0f20af
```

**3. Start Server**
```
python manage.py runserver
```
