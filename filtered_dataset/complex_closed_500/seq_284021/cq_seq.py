import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.0145, -0.015).threePointArc((-0.0105, -0.017), (-0.0065, -0.015)).lineTo(-0.007, -0.015).threePointArc((-0.0105, -0.01661), (-0.014, -0.015)).lineTo(-0.0145, -0.015).close()
solid=wp_sketch0.add(loop0).extrude(0.010738421114655)
