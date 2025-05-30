FROM python:3.10

# -----------------------------------
# switch to root directory
WORKDIR /

# -----------------------------------
# update image os
# Install system dependencies
RUN apt-get update && apt-get install -y \
    ffmpeg \
    libsm6 \
    libxext6 \
    libhdf5-dev \
    && rm -rf /var/lib/apt/lists/*

COPY . .

EXPOSE 5000

RUN apt-get update && apt-get install -y libgl1

# RUN pip install -r requirements.txt

CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "5000", "--reload", "--reload-dir", "/"]