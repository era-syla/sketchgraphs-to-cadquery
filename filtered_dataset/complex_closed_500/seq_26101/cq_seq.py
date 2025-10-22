import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(0.01284, -0.00673).lineTo(0.01284, -0.0047).threePointArc((0.01184, -0.00448), (0.01156, -0.0035)).threePointArc((0.00907, 0.00857), (-0.002, 0.014)).lineTo(-0.043, 0.014).lineTo(-0.043, -0.011).lineTo(-0.042, -0.011).lineTo(-0.042, 0.012).lineTo(-0.03221, 0.012).threePointArc((-0.03897, -0.00088), (-0.03064, -0.01281)).lineTo(-0.0298, -0.011).threePointArc((-0.03675, 0.00245), (-0.025, 0.012)).lineTo(-0.002, 0.012).threePointArc((0.0086, 0.00562), (0.00793, -0.00673)).lineTo(0.01284, -0.00673).close()
solid=wp_sketch0.add(loop0).extrude(0.1525909230300693)
