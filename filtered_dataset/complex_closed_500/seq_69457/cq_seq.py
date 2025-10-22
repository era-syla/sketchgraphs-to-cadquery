import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.02652, 0.01323).lineTo(-0.02652, 0.0).lineTo(-0.03687, 0.0).lineTo(-0.03687, 0.01133).threePointArc((-0.03698, 0.01161), (-0.03727, 0.01173)).lineTo(-0.03734, 0.01173).threePointArc((-0.03738, 0.01176), (-0.03735, 0.0118)).lineTo(-0.02652, 0.01323).close()
solid=wp_sketch0.add(loop0).extrude(-0.01898275900457227)
