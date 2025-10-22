import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(0.0, 0.0).lineTo(0.0, -0.02381).lineTo(0.0, -0.07).lineTo(0.0, 0.0).close()
solid=wp_sketch0.add(loop0).extrude(0.10127960630050457)
