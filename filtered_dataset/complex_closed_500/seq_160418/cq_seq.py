import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(0.322, 0.308).lineTo(0.304, 0.308).lineTo(0.304, 0.078).lineTo(0.322, 0.078).lineTo(0.322, 0.308).close()
solid=wp_sketch0.add(loop0).extrude(0.12299543301156313)
