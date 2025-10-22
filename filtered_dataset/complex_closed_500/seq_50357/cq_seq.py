import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.0065, -0.09).lineTo(-0.0065, -0.08).lineTo(0.0005, -0.08).threePointArc((0.0015, -0.081), (0.0025, -0.08)).lineTo(0.0065, -0.08).lineTo(0.0065, -0.085).lineTo(-0.0015, -0.085).lineTo(-0.0015, -0.09).lineTo(-0.0065, -0.09).close()
solid=wp_sketch0.add(loop0).extrude(0.0008992670545421704)
