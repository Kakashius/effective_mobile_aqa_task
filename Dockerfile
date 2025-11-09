FROM python:3.10

# Системные зависимости
RUN apt-get update \
 && DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
    ca-certificates \
    wget \
    gnupg \
    lsb-release \
    curl \
    unzip \
    jq \
    apt-transport-https \
    fonts-liberation \
    libnss3 \
    libxss1 \
    libasound2 \
    libatk-bridge2.0-0 \
    libgtk-3-0 \
    xvfb \
    xauth \
    dbus-x11 \
    x11-utils \
 && rm -rf /var/lib/apt/lists/*

# Chrome
RUN wget -qO- https://dl-ssl.google.com/linux/linux_signing_key.pub \
    | gpg --dearmor -o /usr/share/keyrings/google-linux-signing-keyring.gpg \
 && echo "deb [arch=amd64 signed-by=/usr/share/keyrings/google-linux-signing-keyring.gpg] http://dl.google.com/linux/chrome/deb/ stable main" \
    > /etc/apt/sources.list.d/google-chrome.list \
 && apt-get update \
 && apt-get install -y --no-install-recommends google-chrome-stable \
 && rm -rf /var/lib/apt/lists/*

# Firefox
RUN apt-get update \
 && apt-get install -y --no-install-recommends firefox-esr \
 && rm -rf /var/lib/apt/lists/*

# ChromeDriver
RUN CHROME_VERSION=$(google-chrome --version | grep -oE '[0-9]+\.') \
 && CHROME_MAIN_VERSION=$(google-chrome --version | grep -oE '[0-9]+' | head -1) \
 && echo "Detected Chrome version: $CHROME_MAIN_VERSION" \
 && CHROMEDRIVER_VERSION=$(curl -s "https://googlechromelabs.github.io/chrome-for-testing/LATEST_RELEASE_${CHROME_MAIN_VERSION}") \
 && echo "Downloading ChromeDriver version: $CHROMEDRIVER_VERSION" \
 && wget -q -O /tmp/chromedriver.zip "https://edgedl.me.gvt1.com/edgedl/chrome/chrome-for-testing/${CHROMEDRIVER_VERSION}/linux64/chromedriver-linux64.zip" \
 && unzip -o /tmp/chromedriver.zip -d /usr/local/bin/ \
 && mv /usr/local/bin/chromedriver-linux64/chromedriver /usr/local/bin/chromedriver \
 && chmod +x /usr/local/bin/chromedriver \
 && rm -rf /tmp/chromedriver.zip /usr/local/bin/chromedriver-linux64

# GeckoDriver
RUN GECKODRIVER_VERSION=$(curl -sS https://api.github.com/repos/mozilla/geckodriver/releases/latest | jq -r '.tag_name' | sed 's/^v//') \
 && wget -q -O /tmp/geckodriver.tar.gz "https://github.com/mozilla/geckodriver/releases/download/v${GECKODRIVER_VERSION}/geckodriver-v${GECKODRIVER_VERSION}-linux64.tar.gz" \
 && tar -xzf /tmp/geckodriver.tar.gz -C /usr/local/bin/ \
 && chmod +x /usr/local/bin/geckodriver \
 && rm /tmp/geckodriver.tar.gz

# Рабочая директория и Python зависимости
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Allure CLI
RUN apt-get update && apt-get install -y default-jre curl
RUN curl -o allure-2.15.0.tgz -Ls https://github.com/allure-framework/allure2/releases/download/2.15.0/allure-2.15.0.tgz \
    && tar -zxvf allure-2.15.0.tgz -C /opt/ \
    && ln -s /opt/allure-2.15.0/bin/allure /usr/bin/allure

# Копирование исходного кода проекта
COPY . .

# Директория для результатов Allure
RUN mkdir -p tests/allure_results tests/allure_report

# Скрипт запуска тестов и генерации отчетов
RUN echo '#!/bin/bash\n\
xvfb-run --auto-servernum --server-args="-screen 0 1920x1080x24" pytest --alluredir=tests/allure_results -s -v ./tests "$@"\n\
allure generate tests/allure_results -o tests/allure_report --clean' > run_tests.sh

RUN chmod +x ./run_tests.sh

ENTRYPOINT ["./run_tests.sh"]
# Браузер по умолчанию
CMD ["--browser=chrome"]