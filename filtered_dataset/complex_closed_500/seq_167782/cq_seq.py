import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.0043, 0.0).lineTo(-0.02278, 0.0).lineTo(-0.02278, 0.013).lineTo(-0.0043, 0.013).lineTo(-0.0043, 0.0).close()
solid=wp_sketch0.add(loop0).extrude(-0.03677093879729178)
