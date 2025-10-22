import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(0.0149, 0.0126).lineTo(-0.0051, 0.0126).lineTo(-0.0051, 0.0074).lineTo(0.0149, 0.0074).threePointArc((0.0175, 0.01), (0.0149, 0.0126)).close()
solid=wp_sketch0.add(loop0).extrude(-0.044780095328861735)
