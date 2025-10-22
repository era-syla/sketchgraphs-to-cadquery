import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.141, 0.051).lineTo(-0.141, 0.051).lineTo(-0.141, -0.051).lineTo(0.141, -0.051).lineTo(0.141, 0.051).close()
solid=wp_sketch0.add(loop0).extrude(0.45748750512190417)
