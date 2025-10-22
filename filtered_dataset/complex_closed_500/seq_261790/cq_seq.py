import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.005, -0.1).lineTo(0.0, -0.1).lineTo(0.0, -0.04).lineTo(-0.005, -0.04).lineTo(-0.005, -0.1).close()
solid=wp_sketch0.add(loop0).extrude(-0.15340806689455763)
