import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.001, -0.00225).lineTo(0.001, -0.00225).lineTo(0.001, 0.00225).lineTo(-0.001, 0.00225).lineTo(-0.001, -0.00225).close()
solid=wp_sketch0.add(loop0).extrude(0.002513749218506535)
