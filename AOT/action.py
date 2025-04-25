from appium.webdriver.common.touch_action import TouchAction

def perform_action(driver, action):
    """Thực hiện hành động trên driver Appium."""
    if action['type'] == 'click':
        element = driver.find_element_by_xpath(action['xpath'])
        element.click()
    elif action['type'] == 'swipe':
        driver.swipe(start_x=action['start_x'], start_y=action['start_y'],
                     end_x=action['end_x'], end_y=action['end_y'], duration=500)
    elif action['type'] == 'drag_and_drop':
        source = driver.find_element_by_xpath(action['source_xpath'])
        target = driver.find_element_by_xpath(action['target_xpath'])
        TouchAction(driver).long_press(source).move_to(target).release().perform()
    elif action['type'] == 'long_press':
        element = driver.find_element_by_xpath(action['xpath'])
        TouchAction(driver).long_press(element, duration=2000).release().perform()