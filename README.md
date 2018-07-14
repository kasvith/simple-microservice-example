# Simple Microservice Example

A very simple microservice example with NodeJS, Python and Docker

## Run the API gateway

- Install `docker` and `docker-compose` according to your operating system

- Clone the repository and navigate to it

- Run `docker-compose up` to start the services

- Try `GET http://YOUR_HOST:3000/api/status` to check whether application is running

## Build the frontend

The application uses a frontend written with plain html with jQuery and to style with Bulma.
This is built with webpack. This default application is built assuming you are using the `localhost`.

To build this to fit your own **IP Address** please follow the steps before you running the `docker-compose up`

- Install NodeJs on your system

- Go to FrontendApplication directory

- Run `npm install` or if you have yarn `yarn` to install packages

- Now you need to set the API Gateway for this frontend application. It can be any host you have. 
    - Let's say you are hosting this application on `http://example.com` then your `API_GATEWAY` would be this one. 
    - If you are hosting in some machine with IP `123.324.345.1` then your `API_GATEWAY` would be your IP.

- To pass this setting to webpack build you need to set an Environment Variable
    - Windows : `set API_GATEWAY=http://YOUR_HOST`
    - Linux/Max : `API_GATEWAY=http://YOUR_HOST`
    * Remember no / at the end of the URL to get your web app work

- Now you can do `npm run build` or `yarn build`

- Check `dist/` folder for newly created index.html and the main.js

- Now run the `docker-compose up` on the root folder of project and check `http://YOUR_HOST:8080` to see web app 

![image](https://user-images.githubusercontent.com/13379595/42726706-82eb0ae6-87b6-11e8-8456-d933b9dfa73b.png)
