# Use the Conda-based Miniconda3 image as a parent image
FROM continuumio/miniconda3

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
    libsqlite3-dev

# Install Python dependencies
#RUN pip install -r requirements.txt

# Create a new Conda environment
RUN conda env create --file environment.yml

# Clean after creation
RUN conda clean -afy

# Create and activate a Conda environment
#RUN conda env create -f environment.yml
SHELL ["conda", "run", "-n", "sda_env", "/bin/bash", "-c"]

# Build your C++ application (adjust the build process as needed)
# only the simulation part not the part needed for ingestion
RUN cd doby/stroman_src/predict/cython_mcss && ./ext_build.sh

#RUN echo "Making sure flask is installed correctly."
#RUN python -c "import flask"

# Expose the port your Flask app will run on
EXPOSE 5000

#Last three lines are pending testing Oct 8.
#RUN conda init bash
#RUN conda activate sda_env
# Specify the command to run your Flask app
#CMD ["python","-m","flask", "--app","doby","--debug","run","--host","0.0.0.0"]
