# BarbershopApp
This is a project for the postgraduate course in Software Engineering at PUC-Minas.

## To run

1. Docker
```
docker build . -t <image-name>
```
```
docker run -it -p 5000:5000 -d <image-name>
```

2. Local
```
python -m venv <env-name>
```
```
source <env-name-path>/bin/activate
```
```
pip install -r requirements.txt
```
```
flask --app src.app run --host 0.0.0.0 --port 5000
```