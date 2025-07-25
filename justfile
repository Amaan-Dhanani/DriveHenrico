
# Starts the docker process
[working-directory: './']
start SERVICE="" *FLAGS:
    bash scripts/before.sh && docker compose up --build -d {{SERVICE}} {{FLAGS}}

# Stops specified docker processes
[working-directory: './']
stop SERVICE="":
    docker compose down {{SERVICE}}

# Starts the docker process in development mode
[working-directory: './']
@dev SERVICE="" *FLAGS:
    bash scripts/before.sh && docker compose -f compose.yml -f dev.compose.yml up --build {{SERVICE}} {{FLAGS}}


# Starts the docker process in testing mode
[working-directory: './']
@test SERVICE="" *FLAGS:
    bash scripts/before.sh && docker compose -f compose.yml -f dev.compose.yml -f test.compose.yml up --build {{SERVICE}} {{FLAGS}}


# Runs the frontend portion of the app
[working-directory: './packages/frontend']
frontend:
    bun run dev

# Runs the backend portiojn
[working-directory: './packages/backend']
backend:
    siblink run .