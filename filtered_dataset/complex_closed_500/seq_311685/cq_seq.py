import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-0.0072, -0.0196).lineTo(-0.0132, -0.0196).lineTo(-0.0132, -0.0326).lineTo(-0.0072, -0.0326).lineTo(-0.0072, -0.0196).close()
solid=wp_sketch0.add(loop0).extrude(0.02772912610586507)
