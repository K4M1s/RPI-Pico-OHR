from menu.menu_item import MenuItem


class SetRangeMAX(MenuItem):

    def __init__(self, display, config):
        super().__init__(display, config, "Ustaw zakr. MAX")
        self.value = config.range_max

    def click(self):
        self.config.range_max = self.value
        self.config.write()

    def up(self):
        if self.value < 65500:
            self.value += 50
        else:
            self.value = 0
        self.render()

    def down(self):
        if self.value > 0:
            self.value -= 50
        else:
            self.value = 65500
        self.render()

    def render(self):
        self.display.lcd.set_cursor_pos(0, 0)
        self.display.lcd.print(self.title)
        self.display.lcd.set_cursor_pos(1, 0)
        self.display.lcd.print('    ')
        self.display.lcd.set_cursor_pos(1, 0)
        self.display.lcd.print(str(self.value))
