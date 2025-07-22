FROM docker:latest

# Install system packages
RUN apk add --no-cache \
    openssh-client \
    git \
    curl \
    jq \
    python3 \
    py3-pip

# Install AWS CLI (allowing system install with PEP 668)
RUN pip3 install awscli --no-cache-dir --break-system-packages

# SSH config (disable host key check for Git/SSH use in CI)
RUN mkdir -p /root/.ssh && \
    chmod 700 /root/.ssh && \
    echo -e "Host *\n\tStrictHostKeyChecking no\n\n" > /root/.ssh/config

# Install latest kubectl (amd64)
RUN curl -LO "https://dl.k8s.io/release/$(curl -Ls https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl" && \
    install -o root -g root -m 0755 kubectl /usr/local/bin/kubectl && \
    rm kubectl
