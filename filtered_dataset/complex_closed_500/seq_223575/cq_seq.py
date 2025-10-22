import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(0.0, 0.0).lineTo(0.0, 0.001).threePointArc((-0.52401, 0.09221), (-0.99828, 0.333)).lineTo(-1.0, 0.333).threePointArc((-0.52498, 0.09147), (-0.0, 0.0)).close()
solid=wp_sketch0.add(loop0).extrude(-0.24665524450194987)
