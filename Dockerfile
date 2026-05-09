# ---- build stage ----
FROM python:3.7-slim AS builder

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    curl \
    git \
    libxrender1 \
    libxext6 \
 && rm -rf /var/lib/apt/lists/*

WORKDIR /build
COPY requirements.txt ./

RUN python -m venv /venv \
 && /venv/bin/pip install --no-cache-dir --upgrade pip \
 && /venv/bin/pip install --no-cache-dir -r requirements.txt \
 && /venv/bin/pip install --no-cache-dir \
    "uvicorn==0.22.0" \
    "google-cloud-storage>=2.0,<3.0"


# ---- runtime stage ----
FROM python:3.7-slim

# Runtime libs only (no compilers)
RUN apt-get update && apt-get install -y --no-install-recommends \
    libxrender1 \
    libxext6 \
 && rm -rf /var/lib/apt/lists/*

# Non-root user required by Cloud Run security policy
RUN useradd --create-home --uid 1000 appuser

WORKDIR /app

# Copy the venv from builder and the source tree
COPY --from=builder /venv /venv
COPY --chown=appuser:appuser src/ ./src/

USER appuser

ENV PATH="/venv/bin:$PATH" \
    PYTHONPATH="/app/src" \
    PYTHONUNBUFFERED=1 \
    CHEMFORMER_N_GPUS=0

# Cloud Run injects PORT; default to 8080
EXPOSE 8080

CMD ["sh", "-c", \
     "uvicorn chemformer.service.retrosynthesis_service:app \
      --host 0.0.0.0 \
      --port ${PORT:-8080} \
      --workers 1"]
