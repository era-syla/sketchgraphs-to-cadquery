import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.042, -0.026).lineTo(0.022, -0.026).threePointArc((0.02766, -0.02834), (0.03, -0.034)).lineTo(0.03, -0.068).threePointArc((0.02766, -0.07366), (0.022, -0.076)).lineTo(-0.042, -0.076).threePointArc((-0.04766, -0.07366), (-0.05, -0.068)).lineTo(-0.05, -0.034).threePointArc((-0.04766, -0.02834), (-0.042, -0.026)).close()
solid=wp_sketch0.add(loop0).extrude(-0.16028959125163805)
