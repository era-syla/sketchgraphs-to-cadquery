import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.00889, 0.01207).lineTo(-0.00889, -0.01207).lineTo(0.00889, -0.01207).lineTo(0.00889, 0.01207).lineTo(-0.00889, 0.01207).close()
solid=wp_sketch0.add(loop0).extrude(-0.018563767683728267)
