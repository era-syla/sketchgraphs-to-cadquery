import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(0.0378, 0.015).lineTo(0.0078, 0.015).lineTo(0.0078, 0.014).threePointArc((0.00824, 0.01294), (0.0093, 0.0125)).lineTo(0.0363, 0.0125).threePointArc((0.03736, 0.01294), (0.0378, 0.014)).lineTo(0.0378, 0.015).close()
solid=wp_sketch0.add(loop0).extrude(-0.07942263081013441)
