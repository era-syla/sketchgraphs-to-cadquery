import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.0, 0.0).lineTo(-0.0381, -0.0).lineTo(-0.0381, -0.00159).threePointArc((-0.03764, -0.00271), (-0.03651, -0.00318)).lineTo(-0.00476, -0.00317).threePointArc((-0.00364, -0.00364), (-0.00318, -0.00476)).lineTo(-0.00317, -0.03651).threePointArc((-0.00271, -0.03764), (-0.00159, -0.0381)).lineTo(0.0, -0.0381).lineTo(0.0, 0.0).close()
solid=wp_sketch0.add(loop0).extrude(0.01256400400060122)
