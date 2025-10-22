import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.19451, 0.00474).threePointArc((-0.19993, 0.00898), (-0.20533, 0.0047)).lineTo(-0.19451, 0.00474).close()
solid=wp_sketch0.add(loop0).extrude(-0.00738202918177442)
