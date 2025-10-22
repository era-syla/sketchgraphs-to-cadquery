import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.0, 0.0).lineTo(0.02223, 0.0).lineTo(0.02222, 0.0127).threePointArc((0.01588, 0.01905), (0.02222, 0.0254)).lineTo(0.02222, 0.0508).threePointArc((0.01587, 0.05715), (0.02222, 0.0635)).lineTo(0.02222, 0.0762).lineTo(-0.0, 0.0762).lineTo(0.0, 0.0).close()
solid=wp_sketch0.add(loop0).extrude(0.22546483731298403)
