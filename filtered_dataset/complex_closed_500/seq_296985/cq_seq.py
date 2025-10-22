import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(0.024, 0.019).lineTo(-0.024, 0.019).lineTo(-0.024, -0.019).lineTo(0.024, -0.019).lineTo(0.024, 0.019).close()
solid=wp_sketch0.add(loop0).extrude(0.13266082911010899)
