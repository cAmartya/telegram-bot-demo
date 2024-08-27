# Use Ubuntu as the base image
FROM ubuntu:latest

# Set environment variables
ENV WINEPREFIX=/wine
ENV WINEARCH=win64

# Update the package list and install necessary packages
RUN apt update && apt-get update
RUN apt-get install -y wget
RUN apt-get install -y wine && apt-get clean

# Download and install Python for Windows using Wine
RUN wget https://www.python.org/ftp/python/3.11.4/python-3.11.4-amd64.exe -O python-installer.exe
RUN wine python-installer.exe /quiet InstallAllUsers=1 PrependPath=1

# Install pip and PyInstaller in the Wine environment
RUN wine ~/.wine/drive_c/users/root/AppData/Local/Programs/Python/Python311/python.exe -m ensurepip && \
    wine ~/.wine/drive_c/users/root/AppData/Local/Programs/Python/Python311/python.exe -m pip install pyinstaller

# Set the working directory inside the container
WORKDIR /src

# Copy your project files into the container
COPY . .

# Build the Windows executable with PyInstaller
RUN wine ~/.wine/drive_c/users/root/AppData/Local/Programs/Python/Python311/python.exe -m PyInstaller --onefile main.py

# After building, the .exe file will be in the /src/dist directory
