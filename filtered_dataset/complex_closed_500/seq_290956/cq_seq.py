import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.0295, -0.01595).lineTo(-0.0295, -0.01595).lineTo(-0.0295, 0.01595).lineTo(0.0295, 0.01595).lineTo(0.0295, -0.01595).close()
solid=wp_sketch0.add(loop0).extrude(0.0652964096067448)
