Tasks
===
### Stage1

    :$ git clone https://github.com/ask4ua/DKN
    :$ docker network create mynet

    Stage1/web:$ docker build ./ -t web
    Stage1/web:$ docker run -p 8080:80 -d --name web --net mynet web

    Stage1/db:$ docker build ./ -t db
    Stage1/db:$ docker run  -d --name db --net mynet db

Remember: some app not as good as should be: webapp trying to connect to db without waiting and retries - and just skeep trying if failed first time.

[Stage1 Diagram](https://github.com/ask4ua/DKN/blob/master/Practices/Section2/Stage1/DevOpsTrainig2-Stage1.png)

### Stage2
    :$ docker run -d --name web1 --net mynet web
    :$ docker run -d --name web2 --net mynet web

    Stage2/proxy:$ docker build ./ -t proxy

    :$ docker run -p 80:80 -d --name proxy --net mynet proxy

[Stage2 Diagram](https://github.com/ask4ua/DKN/blob/master/Practices/Section2/Stage2/DevOpsTrainig2-Stage2.png)

### Stage3
Configure environment like on diagram for Stage3 using configs from Stage2 and Stage1.

    Please try to: provide DB IP (docker --net DNS not working outside of the same host) and Secrets into docker WebApp config by ENV variable on docker run.

[Stage3 Schema](https://github.com/ask4ua/DKN/blob/master/Practices/Section2/Stage3/DevOpsTrainig2-Stage3.png)
