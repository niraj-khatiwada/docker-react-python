FROM node:14-alpine

WORKDIR /usr/app/frontend

COPY package.json package-lock.json ./

RUN npm ci --ignore-scripts

COPY . ./

CMD ["npm", "start"]