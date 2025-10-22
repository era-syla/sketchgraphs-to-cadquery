import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.005, 0.0395).lineTo(0.005, 0.0395).lineTo(0.005, 0.0355).lineTo(-0.005, 0.0355).lineTo(-0.005, 0.0395).close()
solid=wp_sketch0.add(loop0).extrude(-0.01838968150729779)
