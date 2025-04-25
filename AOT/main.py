from driver import get_driver
from state import get_state
from action import perform_action
from reward import get_reward
from agent import QLearningAgent
from logger import logger

# Danh sách hành động
actions = [
    {'type': 'click', 'xpath': '//android.widget.Button[@text="Login"]'},
    {'type': 'swipe', 'start_x': 500, 'start_y': 1000, 'end_x': 500, 'end_y': 100},
    {'type': 'swipe', 'start_x': 500, 'start_y': 100, 'end_x': 500, 'end_y': 1000},
    {'type': 'swipe', 'start_x': 100, 'start_y': 500, 'end_x': 900, 'end_y': 500},
    {'type': 'swipe', 'start_x': 900, 'start_y': 500, 'end_x': 100, 'end_y': 500},
    {'type': 'drag_and_drop', 'source_xpath': '//android.widget.TextView[@text="Item1"]', 
     'target_xpath': '//android.widget.TextView[@text="Item2"]'},
    {'type': 'long_press', 'xpath': '//android.widget.Button[@text="Menu"]'}
]

# Khởi tạo agent
agent = QLearningAgent(actions)

# Huấn luyện
package_path = "/path/to/your/app.apk"  # Thay bằng đường dẫn thực tế
for episode in range(100):
    driver = get_driver(package_path)
    state = get_state(driver)
    done = False
    steps = 0
    logger.info(f"Episode {episode + 1}/100")
    
    while not done and steps < 50:
        action = agent.choose_action(state)
        try:
            perform_action(driver, action)
            error_occurred = False
        except Exception as e:
            logger.error(f"Lỗi xảy ra: {e}")
            error_occurred = True
        
        next_state = get_state(driver)
        reward = get_reward(state, next_state, error_occurred)
        agent.update(state, action, reward, next_state)
        state = next_state
        steps += 1
        
        if error_occurred or steps >= 50:
            done = True
    
    driver.quit()

logger.info("Hoàn tất huấn luyện!")