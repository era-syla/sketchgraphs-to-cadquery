import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-0.05554, 0.08265).lineTo(0.05032, 0.08265).lineTo(0.05032, -0.01034).lineTo(-0.05554, -0.01034).lineTo(-0.05554, 0.08265).close()
solid=wp_sketch0.add(loop0).extrude(-0.18527481845471233)
