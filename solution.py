import pandas as pd
import numpy as np

chat_id = 881258336 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array) -> float:
    y = np.log(x-643)
    return y.mean() 
