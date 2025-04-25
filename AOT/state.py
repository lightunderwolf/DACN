from xml.etree import ElementTree as ET

def get_state(driver):
    """Lấy trạng thái UI từ driver Appium."""
    xml = driver.page_source
    root = ET.fromstring(xml)
    clickable_elements = root.findall(".//*[@clickable='true']")
    scrollable_elements = root.findall(".//*[@scrollable='true']")
    return clickable_elements, scrollable_elements