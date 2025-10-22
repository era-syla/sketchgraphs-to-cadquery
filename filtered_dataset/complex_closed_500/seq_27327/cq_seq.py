import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.06158, -0.036).lineTo(0.06158, -0.036).lineTo(0.06158, 0.0365).lineTo(-0.06158, 0.0365).lineTo(-0.06158, -0.036).close()
solid=wp_sketch0.add(loop0).extrude(0.29438458204466783)
