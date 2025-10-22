import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.05207, 0.0508).lineTo(0.05202, 0.0508).lineTo(0.05202, 0.00762).lineTo(-0.05207, 0.00762).lineTo(-0.05207, 0.0508).close()
solid=wp_sketch0.add(loop0).extrude(-0.27854857724723286)
