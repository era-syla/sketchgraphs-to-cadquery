import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(0.0, 0.0).lineTo(-3.3, 0.0).lineTo(-3.3, -0.5).threePointArc((-1.65, -0.08666), (-0.0, -0.5)).lineTo(0.0, 0.0).close()
solid=wp_sketch0.add(loop0).extrude(-5.984459606482068)
