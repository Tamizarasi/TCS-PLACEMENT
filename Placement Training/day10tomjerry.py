class CartoonNetwork:
    def __init__(self,name,role):
        self.name=name
        self.role=role
    def telecast(self):
        print(self.name,'--',self.role)
    def action(self,act):
        print(f'{self.name} {act}!')
tom=CartoonNetwork('Tom','Cat')
tom.telecast()
tom.action('catches Jerry')
jerry=CartoonNetwork('Jerry','Mouse')
jerry.telecast()
jerry.action('escapes from Tom')
