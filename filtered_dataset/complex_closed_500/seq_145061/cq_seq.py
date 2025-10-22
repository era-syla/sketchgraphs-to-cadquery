import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.009, 0.005).lineTo(0.009, 0.005).lineTo(0.009, -0.005).lineTo(-0.009, -0.005).lineTo(-0.009, 0.005).close()
solid=wp_sketch0.add(loop0).extrude(0.03345772114293343)
