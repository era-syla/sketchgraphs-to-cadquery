import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(2.54, -0.1016).lineTo(-0.1016, -0.1016).lineTo(-0.1016, 2.2352).lineTo(1.9304, 2.2352).lineTo(1.9304, 1.6256).lineTo(2.54, 1.6256).lineTo(2.54, -0.1016).close()
solid=wp_sketch0.add(loop0).extrude(0.4708379548549227)
