import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-0.00192, -0.00019).threePointArc((-0.00242, 0.0218), (-0.00292, -0.00019)).lineTo(-0.00292, -0.006).lineTo(-0.00192, -0.006).lineTo(-0.00192, -0.00019).close()
solid=wp_sketch0.add(loop0).extrude(0.06755145488296392)
