import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.00721, -0.0099).lineTo(0.00779, -0.0099).lineTo(0.00779, 0.0101).lineTo(-0.00721, 0.0101).lineTo(-0.00721, -0.0099).close()
solid=wp_sketch0.add(loop0).extrude(-0.01586052197734424)
