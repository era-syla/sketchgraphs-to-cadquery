import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(0.0, 0.025).threePointArc((-0.025, 0.0), (-0.0, -0.025)).lineTo(0.0, 0.025).close()
solid=wp_sketch0.add(loop0).extrude(-0.022516664937009837)
