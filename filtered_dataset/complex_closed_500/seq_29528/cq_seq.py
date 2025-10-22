import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.0115, -0.0015).threePointArc((-0.013, -0.0), (-0.0115, 0.0015)).lineTo(-0.0245, 0.0015).threePointArc((-0.023, -0.0), (-0.0245, -0.0015)).lineTo(-0.0115, -0.0015).close()
solid=wp_sketch0.add(loop0).extrude(-0.03704339044279502)
