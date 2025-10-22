import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.00319, -0.0116).lineTo(-0.05269, -0.0116).lineTo(-0.05269, -0.0056).lineTo(-0.00319, -0.0056).lineTo(-0.00319, -0.0116).close()
solid=wp_sketch0.add(loop0).extrude(-0.1410645773353146)
