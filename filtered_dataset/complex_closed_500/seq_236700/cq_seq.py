import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.00438, -0.00105).lineTo(-0.00438, -0.00105).threePointArc((-0.0055, -0.00059), (-0.00597, 0.00053)).lineTo(-0.00597, 0.01419).lineTo(0.00597, 0.01419).lineTo(0.00597, 0.00053).threePointArc((0.0055, -0.00059), (0.00438, -0.00105)).close()
solid=wp_sketch0.add(loop0).extrude(-0.016155177455780396)
