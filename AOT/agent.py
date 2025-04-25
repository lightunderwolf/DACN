def get_reward(prev_state, current_state, error_occurred):
    """Tính phần thưởng dựa trên trạng thái và lỗi."""
    if error_occurred:
        return 10
    if current_state != prev_state:
        return 1
    return -0.1