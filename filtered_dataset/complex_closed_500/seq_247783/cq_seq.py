import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(0.0, -0.004).lineTo(-0.006, -0.004).lineTo(-0.006, 0.006).lineTo(-0.013, 0.012).lineTo(-0.013, 0.027).lineTo(-0.006, 0.027).lineTo(-0.006, 0.015).lineTo(0.0, 0.006).lineTo(0.0, 0.0).lineTo(0.0, -0.004).close()
solid=wp_sketch0.add(loop0).extrude(0.008262187854655257)
