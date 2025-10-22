import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.019, 0.009).lineTo(0.019, 0.009).lineTo(0.019, -0.009).lineTo(-0.019, -0.009).lineTo(-0.019, 0.009).close()
solid=wp_sketch0.add(loop0).extrude(-0.024499831357734106)
