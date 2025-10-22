import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-0.03315, 0.0115).lineTo(-0.03315, -0.00355).lineTo(0.00025, -0.00355).lineTo(0.00025, 0.0).threePointArc((0.00375, 0.0035), (0.00725, 0.0)).lineTo(0.00725, -0.0035).lineTo(0.03285, -0.0035).lineTo(0.03285, 0.0115).lineTo(-0.03315, 0.0115).close()
solid=wp_sketch0.add(loop0).extrude(-0.10287209790822992)
