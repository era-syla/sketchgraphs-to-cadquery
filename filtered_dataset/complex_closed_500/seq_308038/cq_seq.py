import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.03104, 0.03399).threePointArc((0.03337, 0.0488), (0.02899, 0.06313)).lineTo(0.02625, 0.06029).threePointArc((0.02886, 0.05335), (0.02967, 0.04598)).lineTo(0.03104, 0.03399).close()
solid=wp_sketch0.add(loop0).extrude(0.08509580540143034)
