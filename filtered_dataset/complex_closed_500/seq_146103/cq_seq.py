import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(0.03695, -0.01334).lineTo(-0.03695, -0.01334).lineTo(-0.03695, 0.01334).lineTo(0.03695, 0.01334).lineTo(0.03695, -0.01334).close()
solid=wp_sketch0.add(loop0).extrude(0.027688463302542574)
