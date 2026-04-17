FROM node:18

WORKDIR /app

COPY package*.json ./
RUN npm install -g pnpm
RUN pnpm install --no-frozen-lockfile

COPY . .

CMD ["pnpm", "start"]
