import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.0075, -0.04041).threePointArc((-0.0125, -0.03541), (-0.0175, -0.04041)).lineTo(-0.0075, -0.04041).close()
solid=wp_sketch0.add(loop0).extrude(-0.007724928204369156)
