import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.11103, 0.05741).lineTo(0.04097, 0.05741).lineTo(0.04097, -0.00059).lineTo(0.07097, -0.00059).lineTo(0.07097, -0.02559).lineTo(0.09297, -0.02559).lineTo(0.09297, -0.00059).lineTo(0.16297, -0.00059).lineTo(0.16297, -0.31759).lineTo(0.09297, -0.31759).lineTo(0.09297, -0.29259).lineTo(0.07097, -0.29259).lineTo(0.07097, -0.31759).lineTo(0.03897, -0.31759).lineTo(0.03897, -0.36759).lineTo(-0.11103, -0.36759).lineTo(-0.11103, 0.05741).close()
solid=wp_sketch0.add(loop0).extrude(-0.46703872949325786)
