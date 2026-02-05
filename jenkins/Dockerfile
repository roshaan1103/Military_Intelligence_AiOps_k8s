FROM jenkins/inbound-agent:latest

USER root

# kubectl
RUN curl -LO https://dl.k8s.io/release/v1.31.2/bin/linux/amd64/kubectl \
 && install -o root -g root -m 0755 kubectl /usr/local/bin/kubectl

# kaniko
RUN mkdir -p /kaniko \
 && curl -L https://github.com/GoogleContainerTools/kaniko/releases/download/v1.23.2/executor \
    -o /kaniko/executor \
 && chmod +x /kaniko/executor

ENV PATH="/kaniko:${PATH}"

USER jenkins

