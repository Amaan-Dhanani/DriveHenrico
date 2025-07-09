
# Starts the docker process
[working-directory: './']
start:
    docker compose up --build -d

# Starts the docker process in development mode
[working-directory: './']
@dev SERVICE="":
    docker compose -f compose.yml -f dev.compose.yml up --build -d {{SERVICE}}
    docker compose logs -f --tail=100 {{SERVICE}}

# Runs the frontend portion of the app
[working-directory: './packages/frontend']
frontend:
    bun run dev


# Runs the backend portiojn
[working-directory: './packages/backend']
backend:
    siblink run .