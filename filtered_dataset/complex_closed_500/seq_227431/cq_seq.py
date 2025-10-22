import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.03384, 0.037).lineTo(-0.0352, 0.037).lineTo(-0.0352, 0.039).lineTo(-0.03384, 0.039).lineTo(-0.03384, 0.037).close()
solid=wp_sketch0.add(loop0).extrude(-0.004549093884557335)
