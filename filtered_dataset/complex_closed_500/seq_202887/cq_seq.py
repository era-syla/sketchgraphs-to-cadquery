import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(0.01957, 0.0).lineTo(-0.02056, 0.0).lineTo(-0.00105, -0.01323).lineTo(-0.00105, -0.01596).lineTo(0.00109, -0.01596).lineTo(0.00109, -0.01323).lineTo(0.01957, -0.0).close()
solid=wp_sketch0.add(loop0).extrude(0.04007680199135213)
