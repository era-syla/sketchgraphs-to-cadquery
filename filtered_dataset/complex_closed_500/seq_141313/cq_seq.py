import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.0, 0.02167).threePointArc((-0.02167, 0.0), (-0.0, -0.02167)).lineTo(0.0, 0.0).lineTo(0.0, 0.02167).close()
solid=wp_sketch0.add(loop0).extrude(0.10496552132632325)
