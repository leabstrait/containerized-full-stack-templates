# Use the official Node.js image as the base image
FROM node:14

# Set the working directory inside the container
WORKDIR /app

# Copy package.json and package-lock.json to the container
COPY package*.json ./

# Install dependencies
RUN npm install

# Copy your server code to the container
COPY index.js .

# Expose the port your WebSocket server will listen on
EXPOSE 8080

# Start your Node.js server
CMD [ "node", "index.js" ]
