import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.0325, 0.043).lineTo(0.0325, 0.043).threePointArc((0.03391, 0.04241), (0.0345, 0.041)).lineTo(0.0345, -0.041).threePointArc((0.03391, -0.04241), (0.0325, -0.043)).lineTo(-0.0325, -0.043).threePointArc((-0.03391, -0.04241), (-0.0345, -0.041)).lineTo(-0.0345, 0.041).threePointArc((-0.03391, 0.04241), (-0.0325, 0.043)).close()
solid=wp_sketch0.add(loop0).extrude(0.17046791407851333)
