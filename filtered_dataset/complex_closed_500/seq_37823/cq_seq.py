import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.04, -0.018).lineTo(-0.04, -0.037).lineTo(-0.03415, -0.037).lineTo(-0.031, -0.03416).lineTo(-0.031, -0.021).threePointArc((-0.03188, -0.01888), (-0.034, -0.018)).lineTo(-0.04, -0.018).close()
solid=wp_sketch0.add(loop0).extrude(-0.038830948246665636)
