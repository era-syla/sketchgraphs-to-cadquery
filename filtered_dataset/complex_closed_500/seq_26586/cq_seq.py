import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(0.0, -0.04472).lineTo(0.05623, 0.01883).lineTo(0.0, 0.01883).lineTo(0.0, -0.04472).close()
solid=wp_sketch0.add(loop0).extrude(-0.1758665779512607)
