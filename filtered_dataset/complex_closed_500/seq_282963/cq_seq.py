import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(0.0, 0.06811).threePointArc((-0.06811, 0.0), (-0.0, -0.06811)).lineTo(0.0, 0.06811).close()
solid=wp_sketch0.add(loop0).extrude(0.24772820336884568)
