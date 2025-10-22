import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.04128, 0.01905).lineTo(-0.04128, 0.01905).threePointArc((-0.04352, 0.01812), (-0.04445, 0.01587)).lineTo(-0.04445, -0.01588).threePointArc((-0.04352, -0.01812), (-0.04128, -0.01905)).lineTo(0.04128, -0.01905).threePointArc((0.04352, -0.01812), (0.04445, -0.01587)).lineTo(0.04445, 0.01588).threePointArc((0.04352, 0.01812), (0.04128, 0.01905)).close()
solid=wp_sketch0.add(loop0).extrude(-0.20215434766855078)
