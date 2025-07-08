
# Starts the docker process
[working-directory: './']
start:
    docker compose up --build -d

# Runs the frontend portion of the app
[working-directory: './packages/frontend']
frontend:
    bun run dev


# Runs the backend portiojn
[working-directory: './packages/backend']
backend:
    siblink run .