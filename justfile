
# Starts the docker process
[working-directory: './']
start:
    bash scripts/before.sh && docker compose up --build -d

# Stops specified docker processes
[working-directory: './']
stop SERVICE="":
    docker compose down {{SERVICE}}

# Starts the docker process in development mode
[working-directory: './']
@dev SERVICE="" *FLAGS:
    bash scripts/before.sh && docker compose -f compose.yml -f dev.compose.yml up --build {{SERVICE}} {{FLAGS}}

# Runs the frontend portion of the app
[working-directory: './packages/frontend']
frontend:
    bun run dev

# Runs the backend portiojn
[working-directory: './packages/backend']
backend:
    siblink run .