# Use the Conda-based Miniconda3 image as a parent image
FROM continuumio/miniconda3

# Set the working directory inside the container
WORKDIR /app

# Install system dependencies for C++ libraries
RUN apt-get update && apt-get install -y \
    build-essential \
    cmake \
    libeigen3-dev \
    libarmadillo-dev \
    sqlite3 \
    libsqlite3-dev

# Copy your Flask application code into the container
COPY . /app

# Create and activate a Conda environment
#RUN conda env create -f environment.yml
#SHELL ["conda", "run", "-n", "sda_env", "/bin/bash", "-c"]

# Install Python dependencies
#RUN pip install -r requirements.txt

# Create a new Conda environment
RUN conda env create --file environment.yml

# Activate the new Conda environment
RUN conda activate sda_env

# Build your C++ application (adjust the build process as needed)
# only the simulation part not the part needed for ingestion
RUN cd doby/stroman_src/predict/cython_mcss && ./ext_build.sh

# Expose the port your Flask app will run on
EXPOSE 5000

# Specify the command to run your Flask app
CMD ["flask", "--app","doby","run"]