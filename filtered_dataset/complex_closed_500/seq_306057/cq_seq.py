import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-0.0369, 0.015).lineTo(0.02958, 0.015).lineTo(0.02958, 0.0).lineTo(-0.0369, 0.0).lineTo(-0.0369, 0.015).close()
solid=wp_sketch0.add(loop0).extrude(-0.11785262713956385)
