# /bin/sh

curl -X POST \
  http://127.0.0.1:8085/slave/checktask \
  -H 'Cache-Control: no-cache' \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -H 'Postman-Token: 9844b8dc-4381-4148-90a8-94d34298fb21' \
  -d 'action=refresh&desc=refresh&task_id=0&params=%7B%22pid%22%3A1%7D'