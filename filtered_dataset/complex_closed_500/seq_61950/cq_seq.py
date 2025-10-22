import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(0.0, 0.0).lineTo(0.508, 0.0).lineTo(0.508, 0.1397).lineTo(-0.0, 0.1397).lineTo(0.0, 0.0).close()
solid=wp_sketch0.add(loop0).extrude(-0.0004105877332743262)
