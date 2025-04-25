import subprocess
import re
from appium import webdriver

def get_apk_info(apk_path):
    """Lấy appPackage và appActivity từ file APK bằng aapt dump badging."""
    result = subprocess.run(["aapt", "dump", "badging", apk_path], capture_output=True, text=True)
    if result.returncode != 0:
        raise Exception(f"Lỗi khi chạy aapt: {result.stderr}")
    
    output = result.stdout
    package_match = re.search(r"package: name='([^']+)'", output)
    activity_match = re.search(r"launchable-activity: name='([^']+)'", output)
    
    if not package_match or not activity_match:
        raise Exception("Không tìm thấy appPackage hoặc appActivity trong output của aapt.")
    
    app_package = package_match.group(1)
    app_activity = activity_match.group(1)
    return app_package, app_activity

def get_driver(package_path):
    """Khởi tạo Appium driver với appPackage và appActivity tự động lấy từ APK."""
    app_package, app_activity = get_apk_info(package_path)
    desired_caps = {
        "platformName": "Android",
        "deviceName": "emulator-5554",
        "appPackage": app_package,
        "appActivity": app_activity,
        "automationName": "UiAutomator2",
        "noReset": True,
    }
    driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)
    return driver