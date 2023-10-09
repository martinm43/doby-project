# Use the Conda-based Miniconda3 image as a parent image
FROM ubuntu:22.04

# Set the working directory inside the container
WORKDIR /app

# Copy your Flask application code into the container
COPY . /app

# Install system dependencies for C++ libraries
RUN apt-get update && apt-get install -y \
    build-essential \
    cmake \
    libeigen3-dev \
    libarmadillo-dev \
    sqlite3 \
    python3 \
    python3-pip \
    libsqlite3-dev && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
RUN pip install -r requirements.txt

# Build your C++ application (adjust the build process as needed)
# only the simulation part not the part needed for ingestion
RUN cd doby/stroman_src/predict/cython_mcss && ./ext_build.sh

# Expose the port your Flask app will run on
EXPOSE 5000

# Specify the command to run your Flask app
CMD ["python","-m","flask", "--app","doby","--debug","run","--host","0.0.0.0"]

