from PyQt6.QtWidgets import QApplication, QGraphicsView, QGraphicsScene, QGraphicsItem, QGraphicsLineItem, QGraphicsEllipseItem, QGraphicsTextItem, QInputDialog, QGraphicsPolygonItem, QGraphicsRectItem
from PyQt6.QtGui import QPen, QBrush, QPainter, QPainterPath, QPolygonF, QTransform 
from PyQt6.QtCore import Qt, QPointF, QLineF
from bus import Bus
from line import Line
from load import Load
from source import Source

import sys


class SLDCanvas(QGraphicsScene):
    def __init__(self):
        super().__init__()
        self.setSceneRect(0, 0, 800, 600)
        self.buses = []
        self.lines = []
        self.loads = []
        self.sources = []

        # Create example buses and lines
        bus1 = Bus(300, 250, "Bus 1", 1.0, 20, 60)
        self.addItem(bus1)
        self.buses.extend([bus1])

        load1 = Load(500, 250, 100, "Load 1")
        self.addItem(load1)
        self.loads.extend([load1])

        source1 = Source(200, 300, 1.0, "Source 1")
        self.addItem(source1)
        self.sources.append(source1)

        source2 = Source(200, 200, 1.0, "Source 2")
        self.addItem(source2)
        self.sources.append(source2)


        line1 = Line(source1, bus1, 0.1, True)
        self.addItem(line1)
        self.lines.append(line1)

        line2 = Line(source2, bus1, 0.1, True)
        self.addItem(line2)
        self.lines.append(line2)

        line3 = Line(bus1, load1, 0.1, True)
        self.addItem(line3)
        self.lines.append(line3)



class SLDApp(QGraphicsView):
    def __init__(self):
        super().__init__()
        self.setScene(SLDCanvas())
        self.setRenderHint(QPainter.RenderHint.Antialiasing)
        self.setDragMode(QGraphicsView.DragMode.RubberBandDrag)
        self.setWindowTitle("SLD Editor")
        self.resize(820, 620)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SLDApp()
    window.show()
    sys.exit(app.exec())
