
class LifeCycle:
    def __init__(self):
        super().__init__()

        self.componentWillMount()
        self.render_()
        self.componentDidMount()
        self.eventHandler_()
        self.translateUI()
        self.destroyComponent()


    def componentWillMount(self): pass
    def render_(self): pass
    def componentDidMount(self): pass
    def eventHandler_(self): pass
    def translateUI(self): pass
    def destroyComponent(self): pass
