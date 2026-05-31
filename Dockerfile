FROM python:3.11-slim

RUN apt-get update && apt-get install -y \
    wget \
    curl \
    make \
    gdebi-core \
    && ARCH=$(dpkg --print-architecture) \
    && wget -q https://github.com/quarto-dev/quarto-cli/releases/download/v1.4.554/quarto-1.4.554-linux-${ARCH}.deb \
    && gdebi --non-interactive quarto-1.4.554-linux-${ARCH}.deb \
    && rm quarto-1.4.554-linux-${ARCH}.deb \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
RUN pip install --no-cache-dir -e .

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

CMD ["make", "report"]
