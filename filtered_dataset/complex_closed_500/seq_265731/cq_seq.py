import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-0.01692, 0.04118).lineTo(-0.00849, 0.03287).lineTo(-0.00845, 0.02991).lineTo(-0.02005, 0.03765).lineTo(-0.03418, 0.03977).lineTo(-0.01692, 0.04118).close()
solid=wp_sketch0.add(loop0).extrude(0.07672734677414689)
