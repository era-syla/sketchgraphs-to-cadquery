import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(7.925, 0.0).lineTo(6.425, -0.0).lineTo(6.425, -0.85).lineTo(7.925, -0.85).lineTo(7.925, 0.0).close()
solid=wp_sketch0.add(loop0).extrude(0.23257535810841246)
