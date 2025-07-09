FROM alpine:3.19

## Install Packages
RUN apk add --update --no-cache python3 git libpq-dev gcc py3-pip python3-dev g++

WORKDIR /backend

# Copy Project
COPY . ./

# Build venv
RUN python -m venv venv

# Activate environment
RUN source /backend/venv/bin/active

# Install requirements
RUN pip install -r requirements.txt

CMD ["python", "main.py"]