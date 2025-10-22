import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(0.2815, 0.028).lineTo(0.2545, 0.028).threePointArc((0.25238, 0.02712), (0.2515, 0.025)).lineTo(0.2515, 0.006).threePointArc((0.25238, 0.00388), (0.2545, 0.003)).lineTo(0.2815, 0.003).lineTo(0.2815, 0.028).close()
solid=wp_sketch0.add(loop0).extrude(-0.02314677946710329)
