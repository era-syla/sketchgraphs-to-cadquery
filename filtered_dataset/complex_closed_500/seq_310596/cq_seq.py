import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(0.024, 0.0275).lineTo(0.01, 0.0).lineTo(0.024, 0.0).lineTo(0.024, 0.0275).close()
solid=wp_sketch0.add(loop0).extrude(0.03042591911905137)
