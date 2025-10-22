import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.1016, 0.18963).lineTo(0.1778, 0.18963).lineTo(0.1778, 0.15153).lineTo(0.12115, 0.15153).threePointArc((0.10206, 0.08625), (0.0508, 0.04155)).lineTo(0.0508, 0.06263).lineTo(0.04919, 0.06263).threePointArc((0.08752, 0.09993), (0.1016, 0.15153)).lineTo(0.1016, 0.18963).close()
solid=wp_sketch0.add(loop0).extrude(0.36617430095739895)
