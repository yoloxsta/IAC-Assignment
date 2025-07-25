# Soe Tintaung's custom pipeline runner image
FROM docker:latest

# Install necessary packages
RUN apk add --no-cache \
    openssh-client \
    git \
    curl \
    jq \
    python3 \
    py3-pip

# Install AWS CLI
RUN pip3 install awscli --no-cache-dir --break-system-packages

# Set up SSH config
RUN mkdir -p ~/.ssh && chmod 700 ~/.ssh && \
    echo -e "Host *\n\tStrictHostKeyChecking no\n\n" > ~/.ssh/config

# Install kubectl (latest version)
RUN curl -L "https://dl.k8s.io/release/$(curl -Ls https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl" -o /usr/local/bin/kubectl && \
    chmod +x /usr/local/bin/kubectl
