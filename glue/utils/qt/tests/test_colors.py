from __future__ import absolute_import, division, print_function

from mock import MagicMock

from glue.external.echo import CallbackProperty
from glue.external.qt import QtGui

from ..helpers import process_dialog
from ..colors import qt4_to_mpl_color, QColorBox, connect_color, QColormapCombo

def test_colors():
    assert qt4_to_mpl_color(QtGui.QColor(255, 0, 0)) == '#ff0000'
    assert qt4_to_mpl_color(QtGui.QColor(255, 255, 255)) == '#ffffff'


# TODO: add a test for the other way around

# TODO: add a test for cmap2pixmap

# TODO: add a test for tint_pixmap

def test_color_box():

    func = MagicMock()

    label = QColorBox()
    label.resize(100,100)
    label.colorChanged.connect(func)
    label.setColor('#472822')

    assert func.call_count == 1


def test_connect_color():

    class FakeClass(object):
        color = CallbackProperty()

    c = FakeClass()

    label = QColorBox()

    connect_color(c, 'color', label)

    label.setColor('#472822')

    assert c.color == '#472822'

    c.color = '#012345'

    assert label.color() == '#012345'


def test_colormap_combo():

    combo = QColormapCombo()
