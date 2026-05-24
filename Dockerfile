FROM python:3.11-slim

# Install Quarto (needed for report generation)
RUN apt-get update && apt-get install -y \
    curl \
    wget \
    gdebi-core \
    && rm -rf /var/lib/apt/lists/*

# Download and install Quarto
RUN wget https://github.com/quarto-dev/quarto-cli/releases/download/v1.3.450/quarto-1.3.450-linux-amd64.deb && \
    gdebi --non-interactive quarto-1.3.450-linux-amd64.deb && \
    rm quarto-1.3.450-linux-amd64.deb

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
ENV PYTHONUNBUFFERED=1
CMD ["/bin/bash"]