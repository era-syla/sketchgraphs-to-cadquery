import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.0331, 0.0615).lineTo(-0.03225, 0.0615).lineTo(-0.03225, 0.0595).lineTo(-0.0331, 0.0595).lineTo(-0.0331, 0.0615).close()
solid=wp_sketch0.add(loop0).extrude(0.00013486692074360918)
