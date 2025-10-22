import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-0.004, 0.0096).lineTo(-0.0024, 0.0096).lineTo(-0.0024, 0.0113).lineTo(0.0024, 0.0113).lineTo(0.0024, 0.0096).lineTo(0.004, 0.0096).lineTo(0.004, 0.0).lineTo(-0.004, -0.0).lineTo(-0.004, 0.0096).close()
solid=wp_sketch0.add(loop0).extrude(0.012665866913094046)
