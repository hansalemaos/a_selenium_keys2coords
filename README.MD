# Send text to coordinates with Selenium

```python
# Tested with:
# https://github.com/ultrafunkamsterdam/undetected-chromedriver
# Python 3.9.13
# Windows 10


$pip install a-selenium-keys2coords

from auto_download_undetected_chromedriver import download_undetected_chromedriver
import undetected_chromedriver as uc

from a_selenium_keys2coords import send_keys_coordinates

if __name__ == "__main__":
    folderchromedriver = "f:\\seleniumdriver3"
    path = download_undetected_chromedriver(
        folder_path_for_exe=folderchromedriver, undetected=True
    )
    driver = uc.Chrome(driver_executable_path=path)
    driver.get(
        r"https://github.com/signup?ref_cta=Sign+up&ref_loc=header+logged+out&ref_page=%2F%3Cuser-name%3E%2F%3Crepo-name%3E&source=header-repo"
    )
    sleep(2)
    send_keys_coordinates(driver, x=300, y=300, text="testest@text.com")
```




