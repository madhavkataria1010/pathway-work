# Pathway Installation Guide

## Overview

This is the inhouse pathway guide for interIIT tech 
---

## Installation Methods

### 1. Using Conda (macOS, Linux & WSL)

To install Pathway using Conda, follow these steps:

1. **Create a Conda Environment**:
   Open your terminal and run:
   ```bash
   conda create -n pathway_env python=3.10
   ```

2. **Activate the Environment**:
   ```bash
   conda activate pathway_env
   ```

3. **Install Pathway**:
   Run the following command to install Pathway:
   ```bash
   pip install -U pathway
   ```

### 2. Using Docker (Any OS)

If you prefer to use Docker, follow these instructions:

1. **Pull the Docker Image**:
   Open your terminal and run:
   ```bash
   docker pull pathwaycom/pathway:latest
   ```

2. **Run the Docker Container**:
   To start the container and access the shell, use:
   ```bash
   docker run -it --entrypoint /bin/bash pathwaycom/pathway:latest
   ```
## Helpful Commands

- **Activate Conda Environment**:
  ```bash
  conda activate pathway_env
  ```

- **List Installed Packages in Conda**:
  ```bash
  conda list
  ```

- **Exit Docker Container**:
  Type `exit` or press `Ctrl + D`.
  
---
## Input Connectors 
![Input Connectors](assets/Input_connectors.png)

## Basic example fort running 
![Input Connectors](assets/basic_eg.png)

