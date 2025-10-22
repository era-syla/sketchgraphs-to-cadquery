import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.09083, 0.0115).lineTo(0.09004, 0.0115).lineTo(0.09004, 0.01093).lineTo(0.09083, 0.01093).lineTo(0.09083, 0.0115).close()
solid=wp_sketch0.add(loop0).extrude(-0.0010205012132528718)
