import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.0099, 0.0006).lineTo(-0.0101, 0.0006).threePointArc((-0.01031, 0.00051), (-0.0104, 0.0003)).lineTo(-0.0104, -0.0003).threePointArc((-0.01031, -0.00051), (-0.0101, -0.0006)).lineTo(-0.0099, -0.0006).threePointArc((-0.00969, -0.00051), (-0.0096, -0.0003)).lineTo(-0.0096, 0.0003).threePointArc((-0.00969, 0.00051), (-0.0099, 0.0006)).close()
solid=wp_sketch0.add(loop0).extrude(5.907640809201798e-05)
