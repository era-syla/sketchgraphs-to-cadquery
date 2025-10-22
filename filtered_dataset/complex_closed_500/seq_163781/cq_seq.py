import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.01422, -0.03175).lineTo(-0.01422, -0.02773).lineTo(-0.01905, -0.02773).lineTo(-0.01905, -0.02388).threePointArc((0.0, -0.02542), (0.01905, -0.02388)).lineTo(0.01905, -0.02769).lineTo(0.01422, -0.02769).lineTo(0.01422, -0.03175).lineTo(-0.01422, -0.03175).close()
solid=wp_sketch0.add(loop0).extrude(-0.09767149142557677)
