import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.17396, -0.1).lineTo(-0.20396, -0.1).threePointArc((-0.21103, -0.09707), (-0.21396, -0.09)).lineTo(-0.21396, 0.09).threePointArc((-0.21103, 0.09707), (-0.20396, 0.1)).lineTo(-0.17396, 0.1).threePointArc((-0.16689, 0.09707), (-0.16396, 0.09)).lineTo(-0.16396, -0.09).threePointArc((-0.16689, -0.09707), (-0.17396, -0.1)).close()
solid=wp_sketch0.add(loop0).extrude(-0.08966669838097589)
