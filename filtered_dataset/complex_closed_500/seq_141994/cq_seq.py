import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.04525, 0.0).lineTo(-0.03125, 0.0).lineTo(-0.03125, 0.0018).lineTo(-0.03375, 0.0018).lineTo(-0.03375, 0.0006).lineTo(-0.04525, 0.0006).lineTo(-0.04525, 0.0).close()
solid=wp_sketch0.add(loop0).extrude(0.017768028536285504)
