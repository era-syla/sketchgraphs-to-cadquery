import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.4, 0.0).lineTo(-0.0, 0.0).lineTo(0.1826, 1.7).lineTo(0.4, 1.7).lineTo(0.4, 0.0).close()
solid=wp_sketch0.add(loop0).extrude(1.3748748061185734)
