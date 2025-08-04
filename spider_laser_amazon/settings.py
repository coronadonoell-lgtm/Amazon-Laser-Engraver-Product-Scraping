BOT_NAME = "spider_laser_amazon"

SPIDER_MODULES = ["spider_laser_amazon.spiders"]
NEWSPIDER_MODULE = "spider_laser_amazon.spiders"

ROBOTSTXT_OBEY = False

# Downloader Middlewares
DOWNLOADER_MIDDLEWARES = {
    'scrapy_selenium.SeleniumMiddleware': 800
}


# Selenium settings
SELENIUM_DRIVER_NAME = "chrome"
SELENIUM_DRIVER_EXECUTABLE_PATH = r"C:\Users\Lhynzkie\Downloads\chromedriver-win64 (1)\chromedriver-win64\chromedriver.exe"
SELENIUM_DRIVER_ARGUMENTS = ['--headless']   # Remove "--headless" to see browser

# ScraperAPI Key
SCRAPERAPI_KEY = 'a147e05ac661ecc123118847c93f2061'

# Random user agents
USER_AGENT_LIST = [
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0 Safari/537.36'
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)...",
    "Mozilla/5.0 (X11; Linux x86_64)..."
]

# CAPTCHA Solver Key (2Captcha)
CAPTCHA_API_KEY = '31879aa5b4480c781a6b5b032ecc06e7'  # Replace with your real key

# Logging
LOG_LEVEL = "INFO"

# Download behavior
CONCURRENT_REQUESTS = 2
DOWNLOAD_DELAY = 2  # adjust for better performance

# Retry settings
RETRY_ENABLED = True
RETRY_TIMES = 3

# Output encoding
FEED_EXPORT_ENCODING = "utf-8"
