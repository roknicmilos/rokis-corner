FROM node:22-alpine

WORKDIR /app

COPY package*.json ./
RUN npm install

COPY build.sh   /app/build.sh
COPY src        /app/src

CMD ["/bin/sh", "/app/build.sh"]
