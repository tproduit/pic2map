# -*- coding: utf-8 -*-
"""
/***************************************************************************
 Pic2Map
                                 A QGIS plugin
 Allow integration of oblique photographies
                             -------------------
        begin                : 2014-02-19
        copyright            : (C) 2014 by Gillian Milani
        email                : gillian.milani@epfl.ch
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""
from pic2Map import Pic2Map

def classFactory(iface):
  return Pic2Map(iface)

