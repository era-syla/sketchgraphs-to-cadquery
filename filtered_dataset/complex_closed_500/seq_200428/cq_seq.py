import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.00895, -0.0279).threePointArc((0.0, -0.0395), (0.00895, -0.0279)).lineTo(0.011, -0.0279).threePointArc((0.0, -0.0415), (-0.011, -0.0279)).lineTo(-0.00895, -0.0279).close()
solid=wp_sketch0.add(loop0).extrude(0.02387078501421326)
