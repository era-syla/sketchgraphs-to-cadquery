import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.021, 0.049).lineTo(0.008, 0.049).threePointArc((0.00234, 0.04666), (0.0, 0.041)).lineTo(0.0, 0.028).lineTo(-0.004, 0.028).lineTo(-0.004, 0.053).lineTo(0.021, 0.053).lineTo(0.021, 0.049).close()
solid=wp_sketch0.add(loop0).extrude(0.045270490821550574)
