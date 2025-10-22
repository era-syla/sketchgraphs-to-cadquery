import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(0.005, 0.01575).threePointArc((0.00475, 0.016), (0.005, 0.01625)).lineTo(0.0, 0.01625).threePointArc((0.00025, 0.016), (-0.0, 0.01575)).lineTo(0.005, 0.01575).close()
solid=wp_sketch0.add(loop0).extrude(-0.0005044217864694333)
