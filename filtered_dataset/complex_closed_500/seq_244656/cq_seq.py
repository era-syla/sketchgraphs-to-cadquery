import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.0, 0.0).lineTo(0.0778, 0.0).lineTo(0.0778, 0.1593).lineTo(-0.0, 0.1593).lineTo(0.0, 0.0).close()
solid=wp_sketch0.add(loop0).extrude(0.4613240294487503)
