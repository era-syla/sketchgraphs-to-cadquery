import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.11747, 0.00635).lineTo(0.0762, 0.00635).lineTo(0.0762, 0.01905).lineTo(0.11747, 0.01905).lineTo(0.11747, 0.00635).close()
solid=wp_sketch0.add(loop0).extrude(-0.10879807365195189)
