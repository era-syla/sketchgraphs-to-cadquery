import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.005, -0.00945).lineTo(0.005, -0.00945).lineTo(0.005, -0.00145).lineTo(-0.005, -0.00145).lineTo(-0.005, -0.00945).close()
solid=wp_sketch0.add(loop0).extrude(-0.001885392216238442)
