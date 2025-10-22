import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.027, 0.0145).lineTo(0.027, 0.0145).lineTo(0.027, -0.0145).lineTo(-0.027, -0.0145).lineTo(-0.027, 0.0145).close()
solid=wp_sketch0.add(loop0).extrude(0.009734014435131055)
