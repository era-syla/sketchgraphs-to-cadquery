import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.06455, 0.0026).lineTo(-0.06685, 0.0049).lineTo(-0.06285, 0.0049).lineTo(-0.06055, 0.0026).lineTo(-0.06455, 0.0026).close()
solid=wp_sketch0.add(loop0).extrude(0.016293789115987677)
