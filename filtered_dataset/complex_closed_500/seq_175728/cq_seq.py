import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(0.00965, 0.0381).lineTo(0.02235, 0.0381).lineTo(0.02235, 0.03175).lineTo(0.00965, 0.03175).lineTo(0.00965, 0.0381).close()
solid=wp_sketch0.add(loop0).extrude(0.03450743034125609)
