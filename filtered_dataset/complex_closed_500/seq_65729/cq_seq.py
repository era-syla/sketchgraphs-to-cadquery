import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(0.03385, -0.013).threePointArc((0.03502, -0.01252), (0.0355, -0.01135)).lineTo(0.0355, 0.01135).threePointArc((0.03502, 0.01252), (0.03385, 0.013)).lineTo(-0.03385, 0.013).threePointArc((-0.03502, 0.01252), (-0.0355, 0.01135)).lineTo(-0.0355, -0.01135).threePointArc((-0.03502, -0.01252), (-0.03385, -0.013)).lineTo(0.03385, -0.013).close()
solid=wp_sketch0.add(loop0).extrude(-0.11252738585535187)
