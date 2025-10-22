import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(0.03729, 0.01605).threePointArc((0.03469, 0.01865), (0.03209, 0.01605)).threePointArc((0.03209, 0.01549), (0.03208, 0.01493)).threePointArc((0.03237, 0.01462), (0.03206, 0.01433)).threePointArc((0.02893, -0.00096), (0.02097, -0.01439)).lineTo(0.02621, -0.01619).threePointArc((0.03413, -0.0019), (0.03726, 0.01412)).threePointArc((0.03762, 0.01446), (0.03728, 0.01482)).threePointArc((0.03729, 0.01544), (0.03729, 0.01605)).close()
solid=wp_sketch0.add(loop0).extrude(-0.07723149234557569)
