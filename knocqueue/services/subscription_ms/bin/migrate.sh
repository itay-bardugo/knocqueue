docker exec docker-services_subscription-ms_1 bash -c ' \
flask db init
flask db migrate
'
sleep 3