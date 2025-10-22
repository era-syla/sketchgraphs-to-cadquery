import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(0.0215, 0.00304).lineTo(-0.0215, 0.00304).lineTo(-0.0215, 0.00534).lineTo(0.0, 0.01504).lineTo(0.0215, 0.00534).lineTo(0.0215, 0.00304).close()
solid=wp_sketch0.add(loop0).extrude(-0.014283455708042582)
