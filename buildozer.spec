name: Build Android APK

on:
  push:
    branches: [main]
  workflow_dispatch:

jobs:
  build:
    runs-on: ubuntu-22.04

    steps:
      - name: Checkout
        uses: actions/checkout@v4

      - name: Setup Java
        uses: actions/setup-java@v4
        with:
          distribution: temurin
          java-version: '17'

      - name: Setup Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.10'

      - name: Install dependencies
        run: |
          sudo apt update
          sudo apt install -y git zip unzip autoconf libtool \
            pkg-config zlib1g-dev libncurses5-dev libtinfo5 \
            cmake libffi-dev libssl-dev automake

      - name: Install Buildozer
        run: |
          pip install --upgrade pip
          pip install buildozer setuptools Cython==0.29.34

      - name: Build APK
        run: |
          buildozer -v android debug

      - name: Upload APK
        uses: actions/upload-artifact@v4
        with:
          name: My-Calculator-APK
          path: bin/*.apk
