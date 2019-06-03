# ---- Python base ----
FROM python:3.7.3-slim AS base

# ---- Dependencias del sistema
FROM base AS system-base

RUN apt-get update && apt-get upgrade

# RUN apt-get update && apt-get install -y \
#     binutils \
#     libproj-dev \
#     gdal-bin \
#     graphviz \
#     libgraphviz-dev \
#     pkg-config \
#     && rm -rf /var/lib/apt/lists/*

RUN mkdir /app
COPY ./requirements.txt /app/
RUN pip install --upgrade pip \
    && pip install -r /app/requirements.txt

COPY ./start.sh /start.sh
# COPY ./wait_for_postgres.sh /wait_for_postgres.sh
# RUN chmod +x /start.sh && chmod +x /wait_for_postgres.sh && mkdir /logs
RUN chmod +x /start.sh && chmod +x /wait_for_postgres.sh && mkdir /logs

COPY ./src /app/

# ---- Compilación final para producción
FROM system-base as release

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


COPY --from=system-base /root/.cache /root/.cache
COPY --from=system-base /app/requirements.txt /app/
RUN pip install -r /app/requirements/prod.txt && rm -rf /root/.cache

WORKDIR /app

# ---- Versión de desarrollo
FROM dependencies AS develop

RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

COPY --from=dependencies /root/.cache /root/.cache
COPY --from=dependencies /app/requirements/base.txt /app/requirements/
COPY ./requirements/dev.txt /app/requirements/
RUN pip install -r /app/requirements/dev.txt && rm -rf /root/.cache

COPY ./run_tests.sh /app/

WORKDIR /app/src
