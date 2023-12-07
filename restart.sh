sudo docker stop my_django_app_web_1 && \
sudo docker stop my_django_app_nginx_1 && \
sudo docker rm my_django_app_nginx_1 && \
sudo docker rm my_django_app_web_1 && \
sudo docker rmi my_django_app_web:latest && \
sudo docker rmi my_django_app_nginx:latest && \
docker-compose -f docker-compose.prod.yml up -d
