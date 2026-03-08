# For more info see https://github.com/BurnySc2/python-sc2-docker
FROM burnysc2/python-sc2-docker:py_3.14-sc2_4.10-v1.0.7 AS base

# Install Open Code
RUN curl -fsSL https://opencode.ai/install | bash

ENTRYPOINT [ "/bin/bash" ]