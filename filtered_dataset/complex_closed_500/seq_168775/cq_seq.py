import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(0.0165, -0.05039).threePointArc((0.01956, -0.04835), (0.01752, -0.04529)).lineTo(0.01701, -0.04784).lineTo(0.0165, -0.05039).close()
solid=wp_sketch0.add(loop0).extrude(-0.005120631800450981)
