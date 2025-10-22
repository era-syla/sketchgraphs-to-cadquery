import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(0.0, -0.02).lineTo(0.06, -0.02).lineTo(0.06, -0.06).lineTo(0.0, -0.06).lineTo(0.0, -0.02).close()
solid=wp_sketch0.add(loop0).extrude(0.015686232512601615)
