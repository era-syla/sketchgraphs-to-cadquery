import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.09, 0.08).threePointArc((0.075, 0.095), (0.06, 0.08)).lineTo(0.06, 0.0346).threePointArc((0.075, 0.0196), (0.09, 0.0346)).lineTo(0.09, 0.08).close()
solid=wp_sketch0.add(loop0).extrude(0.2251466080417332)
