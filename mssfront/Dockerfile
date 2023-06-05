FROM node:lts-alpine

WORKDIR /front

COPY ./mssfront .

RUN npm install -g npm\
    && npm install

EXPOSE 8080

COPY ./mssfront/entrypoint.sh  /front//entrypoint.sh

RUN chmod +x /front/entrypoint.sh

ENTRYPOINT ["sh","/front/entrypoint.sh" ]