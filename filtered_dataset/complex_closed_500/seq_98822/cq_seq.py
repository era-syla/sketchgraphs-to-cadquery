import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.21812, -0.0).lineTo(0.0, 0.01905).threePointArc((0.01905, -0.0), (0.0, -0.01905)).lineTo(-0.21812, -0.01905).threePointArc((-0.20859, -0.00953), (-0.21812, 0.0)).close()
solid=wp_sketch0.add(loop0).extrude(0.06857873823280868)
