docker build -t notification_service .
docker tag notification_service:latest 590183763314.dkr.ecr.eu-central-1.amazonaws.com/notification_service:latest
docker push 590183763314.dkr.ecr.eu-central-1.amazonaws.com/notification_service:latest
