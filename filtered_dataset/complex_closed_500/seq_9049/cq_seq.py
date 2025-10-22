import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.00586, 0.01409).lineTo(0.05614, 0.01409).lineTo(0.05614, -0.04391).lineTo(-0.00586, -0.04391).lineTo(-0.00586, 0.01409).close()
solid=wp_sketch0.add(loop0).extrude(0.0757952253653427)
