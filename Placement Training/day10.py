class ClickPen:
    def __init__ (self,colour):
        self.colour=colour
    is_click=False
    def click(self):
        is_click=not is_click
    def write(self,text):
        if is_click:
            print(f'Writing,{text} in {self.colour}')
        else:
            print('Cannot write!')
pen=ClickPen('Blue')
pen.write('Hello...')
pen.click()

