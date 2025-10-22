import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.04554, -0.01125).lineTo(0.00889, 0.03593).lineTo(0.0597, 0.01198).lineTo(-0.04554, -0.01125).close()
solid=wp_sketch0.add(loop0).extrude(0.11586075225513402)
