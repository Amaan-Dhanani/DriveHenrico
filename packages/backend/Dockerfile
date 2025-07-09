FROM alpine:3.19

## Install Packages
RUN apk add --update --no-cache python3 git libpq-dev gcc py3-pip python3-dev g++ py3-virtualenv

# Copy Project

WORKDIR /backend

COPY . ./

# Build venv using virtualenv (ensures pip is present)
RUN python3 -m virtualenv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

# Install requirements using the venv's pip
RUN /opt/venv/bin/pip install --upgrade pip && /opt/venv/bin/pip install -r requirements.txt

CMD ["/opt/venv/bin/python", "/backend/main.py"]