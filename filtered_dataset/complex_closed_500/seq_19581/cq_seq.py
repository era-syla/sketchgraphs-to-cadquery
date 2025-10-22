import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(0.05614, 0.089).lineTo(0.065, 0.089).threePointArc((0.06854, 0.08754), (0.07, 0.084)).lineTo(0.07, 0.07465).threePointArc((0.06876, 0.07135), (0.06565, 0.06969)).lineTo(0.05518, 0.06831).threePointArc((0.05096, 0.06977), (0.04958, 0.07401)).lineTo(0.0512, 0.08475).threePointArc((0.05288, 0.08779), (0.05614, 0.089)).close()
solid=wp_sketch0.add(loop0).extrude(0.05143480299450299)
