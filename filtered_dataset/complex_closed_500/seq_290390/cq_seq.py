import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.006, 0.0175).threePointArc((0.0, 0.0235), (-0.006, 0.0175)).lineTo(-0.006, -0.0175).threePointArc((0.0, -0.0235), (0.006, -0.0175)).lineTo(0.006, 0.0175).close()
solid=wp_sketch0.add(loop0).extrude(-0.0377160415024825)
