from PyQt6.QtWidgets import QApplication, QGraphicsView, QGraphicsScene
from PyQt6.QtGui import QPainter

from sld_data import bus_data, line_data, source_data, load_data

from bus import Bus
from line import Line
from load import Load
from source import Source

import sys



class SLDCanvas(QGraphicsScene):
    def __init__(self):
        super().__init__()
        self.setSceneRect(0, 0, 800, 600)
        self.buses = {}
        self.lines = []
        self.loads = {}
        self.sources = {}

        # Create example buses and lines

        for data in bus_data:
            bus = Bus(data["x"], data["y"], data["name"], data["voltage"], data["angle"], data["width"], data["height"])
            self.addItem(bus)
            self.buses[data["name"]] = bus
        
        for data in source_data:
            source = Source(data["x"], data["y"], data["voltage"], data["name"])
            self.addItem(source)
            self.sources[data["name"]] = source
        
        for data in load_data:
            load = Load(data["x"], data["y"], data["power"], data["name"])
            self.addItem(load)
            self.loads[data["name"]] = load
        


        for data in line_data:
            item1 = self.buses.get(data["item1"]) or self.sources.get(data["item1"]) or self.loads.get(data["item1"])
            item2 = self.buses.get(data["item2"]) or self.sources.get(data["item2"]) or self.loads.get(data["item2"])

            if item1 and item2:
                print(f"Connecting {item1.name} to {item2.name}")
                line = Line(data["name"], item1, item2, data["impedance"], data["is_directed"])
                self.addItem(line)
                self.lines.append(line)

            

        # bus1 = Bus(300, 250, "Bus 1", 1.0, 20, 60)
        # self.addItem(bus1)
        # self.buses.extend([bus1])

        # load1 = Load(500, 250, 100, "Load 1")
        # self.addItem(load1)
        # self.loads.extend([load1])

        # source1 = Source(200, 300, 1.0, "Source 1")
        # self.addItem(source1)
        # self.sources.append(source1)

        # source2 = Source(200, 200, 1.0, "Source 2")
        # self.addItem(source2)
        # self.sources.append(source2)

        # line0 = Line(source1, bus1, 0.1, True)
        # self.addItem(line0)
        # self.lines.append(line0)

        # line1 = Line(source1, bus1, 0.1, True)
        # self.addItem(line1)
        # self.lines.append(line1)

        # line2 = Line(source2, bus1, 0.1, True)
        # self.addItem(line2)
        # self.lines.append(line2)

        # line3 = Line(bus1, load1, 0.1, True)
        # self.addItem(line3)
        # self.lines.append(line3)



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
