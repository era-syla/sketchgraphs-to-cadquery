import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(0.0, -0.0001).threePointArc((0.0001, 0.0), (0.0, 0.0001)).lineTo(0.0, -0.0001).close()
solid=wp_sketch0.add(loop0).extrude(0.0005599595682017427)
