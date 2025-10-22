import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.635, 0.56182).lineTo(-0.654, 0.56182).lineTo(-0.654, 0.49382).lineTo(-0.635, 0.49382).lineTo(-0.635, 0.56182).close()
solid=wp_sketch0.add(loop0).extrude(-0.16791927578198282)
