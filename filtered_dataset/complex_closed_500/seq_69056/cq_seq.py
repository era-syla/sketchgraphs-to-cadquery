import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(0.0, 0.0).lineTo(0.0, -0.76).lineTo(0.03, -0.76).lineTo(0.03, -0.6).lineTo(0.035, -0.6).lineTo(0.035, -0.44).lineTo(0.04, -0.44).lineTo(0.04, 0.0).lineTo(0.0, 0.0).close()
solid=wp_sketch0.add(loop0).extrude(-1.9129143529705934)
