FROM python:3.5-slim
MAINTAINER Rob Hudson <robhudson@mozilla.com>

ENV PYTHONUNBUFFERED=1 \
    PYTHONPATH=/app/ \
    PORT=8000

EXPOSE $PORT

# Add a non-privileged user for installing and running the application.
# Don't use --create-home option to prevent populating with skeleton files.
RUN mkdir /app && \
    chown 10001:10001 /app && \
    groupadd --gid 10001 app && \
    useradd --no-create-home --uid 10001 --gid 10001 --home-dir /app app

# Install a few essentials and clean apt caches afterwards.
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        build-essential \
        curl \
        git && \
    apt-get autoremove -y && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# Install Python dependencies.
COPY requirements.txt /tmp/
# Switch to /tmp to install dependencies outside home dir.
WORKDIR /tmp
RUN pip3 install --no-cache-dir -r requirements.txt

# Switch back to home directory.
WORKDIR /app

USER 10001

# Using /bin/bash as the entrypoint works around some volume mount issues on
# Windows where volume-mounted files do not have execute bits set.
# https://github.com/docker/compose/issues/2301#issuecomment-154450785 has additional background.
ENTRYPOINT ["/bin/bash", "/app/bin/run"]

CMD ["web"]
