import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-0.0, 0.0462).threePointArc((-0.00221, 0.04589), (-0.00425, 0.04498)).threePointArc((-0.01891, 0.03317), (-0.03041, 0.01827)).threePointArc((-0.03253, 0.01333), (-0.03325, 0.008)).lineTo(-0.03325, -0.0).lineTo(0.0, 0.0).lineTo(0.0, 0.0462).close()
solid=wp_sketch0.add(loop0).extrude(-0.035516734016039504)
