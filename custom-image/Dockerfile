FROM docker:23-dind

RUN apk add --no-cache \
    openssh-client \
    git \
    curl \
    jq \
    python3 \
    py3-pip \
 && pip3 install awscli --no-cache-dir --break-system-packages \
 && curl -L "https://dl.k8s.io/release/$(curl -Ls https://dl.k8s.io/release/stable.txt)/bin/linux/$(uname -m)/kubectl" \
    -o /usr/local/bin/kubectl \
 && chmod +x /usr/local/bin/kubectl
