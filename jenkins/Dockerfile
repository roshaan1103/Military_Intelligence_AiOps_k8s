FROM jenkins/jenkins:lts

USER root

# Install dependencies
RUN apt-get update && \
    apt-get install -y curl ca-certificates gnupg && \
    curl -LO https://dl.k8s.io/release/v1.31.2/bin/linux/amd64/kubectl && \
    install -o root -g root -m 0755 kubectl /usr/local/bin/kubectl && \
    rm kubectl

# Verify
RUN kubectl version --client

USER jenkins
