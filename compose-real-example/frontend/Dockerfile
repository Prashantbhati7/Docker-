FROM node:20-alpine

WORKDIR /myApp

COPY package*.json package-lock.json ./

RUN npm install

COPY ./src ./src

COPY jsconfig.json ./
COPY eslint.config.mjs ./
COPY next.config.mjs ./
COPY postcss.config.mjs ./
EXPOSE 3000


CMD ["npm", "run", "dev"]