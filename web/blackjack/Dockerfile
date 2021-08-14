FROM node:latest AS build
WORKDIR /app
COPY ./ /app/
RUN npm install
RUN npm run build:prod

FROM nginx:latest
COPY --from=build /app/dist/blackjack /usr/share/nginx/html
EXPOSE 80
