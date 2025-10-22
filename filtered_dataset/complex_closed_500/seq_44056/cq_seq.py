import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.0, 0.0).lineTo(-0.05, 0.0).lineTo(-0.05, 0.05).lineTo(-0.045, 0.05).lineTo(-0.045, 0.012).threePointArc((-0.04295, 0.00705), (-0.038, 0.005)).lineTo(0.0, 0.005).lineTo(0.0, 0.0).close()
solid=wp_sketch0.add(loop0).extrude(0.07029044207009223)
