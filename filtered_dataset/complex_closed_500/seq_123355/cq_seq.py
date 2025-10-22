import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-0.00602, -0.0048).lineTo(0.00602, -0.0048).threePointArc((0.00673, -0.0045), (0.00702, -0.0038)).lineTo(0.00702, 0.0038).threePointArc((0.00673, 0.0045), (0.00602, 0.0048)).lineTo(-0.00602, 0.0048).threePointArc((-0.00673, 0.0045), (-0.00702, 0.0038)).lineTo(-0.00702, -0.0038).threePointArc((-0.00673, -0.0045), (-0.00602, -0.0048)).close()
solid=wp_sketch0.add(loop0).extrude(0.0210489319431934)
