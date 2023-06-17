echo "Iniciando aplicação"

sleep 1h

uvicorn src.main:app --host 0.0.0.0 --port $PORT