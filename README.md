# Pathway

## Working with Pathway

### Installation (macOS, Linux & WSL)

1. **Create a Conda environment**:
   ```bash
   conda create --name pathway-env python=3.8
   conda activate pathway-env

	2.	Install Pathway:
Use the following command to install Pathway via pip:

pip install -U pathway



2. **Using Docker (Any OS)**:

	1.	Pull the Docker image:

docker pull pathwaycom/pathway:latest


	2.	Run the Docker container:
Start the container with an interactive Bash shell:

docker run -it --entrypoint /bin/bash pathwaycom/pathway:latest

