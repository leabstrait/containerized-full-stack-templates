# Stage 1: Build the Vue.js application
FROM node:14-alpine AS build-stage

WORKDIR /app

# Copy package.json and package-lock.json to the container
COPY package*.json ./

# Install Node.js dependencies
RUN npm install

# Copy the rest of your Vue.js application code to the container
COPY . .

# Build your Vue.js application for production
RUN npm run build

