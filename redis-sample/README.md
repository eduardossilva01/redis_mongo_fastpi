# MongoDB Server Container
```
docker run -d \
    --name=mongo \
    --restart=unless-stopped \
    -e MONGO_INITDB_ROOT_USERNAME=admin \
    -e MONGO_INITDB_ROOT_PASSWORD=password123 \
    -p 27017:27017 \
    mongo
```
# Redis Container
```
docker run -d \
    --name=redis \
    --restart=unless-stopped \
    -p 6379:6379 \
    redis
```
# Se não tiver PIP ou Python3 instalado
```
sudo apt install -y python3 python3-pip python-is-python3
```

# Se não tiver o poetry instalado
```
pip install poetry
```

# Ativar venv (dentro do diretório do projeto)
```
poetry shell
```

# Instalar dependências (apenas na primeira vez)
```
poetry install
```

# Rodar a api
```
python redis_sample/api.py
```
