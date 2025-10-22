import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.0197, 0.0054).lineTo(-0.0177, 0.0054).lineTo(-0.0197, 0.0034).lineTo(-0.0197, 0.0054).close()
solid=wp_sketch0.add(loop0).extrude(-0.0025007518599518587)
