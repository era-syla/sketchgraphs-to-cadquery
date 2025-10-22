import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.024, -0.0215).lineTo(-0.025, -0.0215).threePointArc((-0.02641, -0.02091), (-0.027, -0.0195)).lineTo(-0.027, -0.0165).threePointArc((-0.02641, -0.01509), (-0.025, -0.0145)).lineTo(-0.024, -0.0145).threePointArc((-0.02259, -0.01509), (-0.022, -0.0165)).lineTo(-0.022, -0.0195).threePointArc((-0.02259, -0.02091), (-0.024, -0.0215)).close()
solid=wp_sketch0.add(loop0).extrude(0.01340871132617861)
