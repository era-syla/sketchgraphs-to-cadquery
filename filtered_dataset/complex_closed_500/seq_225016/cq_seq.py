import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.1778, 0.00635).threePointArc((0.17047, 0.01105), (0.16193, 0.0127)).lineTo(0.1778, 0.0127).lineTo(0.1778, 0.00635).close()
solid=wp_sketch0.add(loop0).extrude(0.03702267438389652)
