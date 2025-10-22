import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.048, 0.0215).lineTo(0.052, 0.0215).lineTo(0.052, -0.0285).lineTo(-0.048, -0.0285).lineTo(-0.048, 0.0215).close()
solid=wp_sketch0.add(loop0).extrude(0.04331447977068042)
