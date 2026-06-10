FROM node:20-alpine

WORKDIR /myApp

COPY package*.json ./


RUN npm install

COPY ./index.js ./


EXPOSE 3001

CMD ["npm","run","dev"]