import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(0.0015, 0.001).lineTo(-0.0015, 0.001).threePointArc((-0.00157, 0.00097), (-0.0016, 0.0009)).lineTo(-0.0016, -0.0009).threePointArc((-0.00157, -0.00097), (-0.0015, -0.001)).lineTo(0.0015, -0.001).threePointArc((0.00157, -0.00097), (0.0016, -0.0009)).lineTo(0.0016, 0.0009).threePointArc((0.00157, 0.00097), (0.0015, 0.001)).close()
solid=wp_sketch0.add(loop0).extrude(0.007752745445912604)
