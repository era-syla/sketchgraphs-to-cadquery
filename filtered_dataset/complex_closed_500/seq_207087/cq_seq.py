import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.04427, 0.03538).threePointArc((0.02784, 0.05156), (0.01158, 0.03522)).lineTo(0.01319, 0.03522).threePointArc((0.02819, 0.05038), (0.04335, 0.03538)).lineTo(0.04427, 0.03538).close()
solid=wp_sketch0.add(loop0).extrude(0.06477680161442957)
