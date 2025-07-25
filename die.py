from random import randint

class Die:
    """表示一个骰子"""
    
    def __init__(self, num_sides=6):
        """骰子默认有6个面"""
        self.num_sides = num_sides

    def roll(self):
        """返回一个随机值，范围从1到骰子的面数"""
        return randint(1, self.num_sides)