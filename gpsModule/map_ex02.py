import io
import sys
import folium
# pip install PyQt5 + pip install PyQtWebEngine
from PyQt5 import QtWidgets, QtWeb

app = QtWidgets.QApplication(sys.argv) 
m = folium.Map(location=[35.1168, 129.0926], zoom_start=12)

data = io.BytesIO()
m.save(data, close_file='False')

widgets = QtWebEngineWidgets.None
widgets.setHtml(data.getValue().decode())
widgets.resize(800, 600)
widgets.show()

sys.exit(app.exec_())
