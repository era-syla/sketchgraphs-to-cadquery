import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(0.08617, -0.09329).threePointArc((-0.0, 0.127), (-0.08617, -0.09329)).lineTo(-0.08299, -0.08974).threePointArc((-0.0, 0.12224), (0.08299, -0.08974)).lineTo(0.08617, -0.09329).close()
solid=wp_sketch0.add(loop0).extrude(-0.2627451972322796)
