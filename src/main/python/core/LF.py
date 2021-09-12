
from PyQt5.QtCore import Qt

class LifeCycle:
    def __init__(self):
        super().__init__()

        self.componentWillMount()
        self.allowBackground()
        self.render_()
        self.componentDidMount()
        self.loadCSS()
        self.responsiveUI()

    def componentWillMount(self): pass
    def allowBackground(self):
        self.setAttribute(Qt.WA_StyledBackground, True)
    def render_(self): pass
    def resizeEvent(self, e=None): pass
    def responsiveUI(self): pass
    def destroyComponent(self): pass
    def loadCSS(self): pass
    def componentDidMount(self): pass

    @staticmethod
    def pct(a,b): return int((a * b) / 100.0)
