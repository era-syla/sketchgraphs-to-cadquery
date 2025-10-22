import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.01718, 0.05478).lineTo(0.00822, 0.05478).lineTo(0.00822, 0.01033).lineTo(-0.01718, 0.01033).lineTo(-0.01718, 0.05478).close()
solid=wp_sketch0.add(loop0).extrude(0.07356338798142201)
