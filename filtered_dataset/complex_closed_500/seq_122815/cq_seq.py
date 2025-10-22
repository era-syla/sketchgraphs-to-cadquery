import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.004, -0.09).lineTo(0.004, -0.09).lineTo(0.004, -0.086).lineTo(-0.004, -0.086).lineTo(-0.004, -0.09).close()
solid=wp_sketch0.add(loop0).extrude(0.0073634754650858765)
