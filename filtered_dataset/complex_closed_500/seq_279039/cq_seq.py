import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.0, 0.0381).lineTo(0.0, 0.0).lineTo(0.03938, 0.0).lineTo(0.03938, -0.03668).lineTo(-0.03824, -0.03668).lineTo(-0.03824, 0.0381).lineTo(0.0, 0.0381).close()
solid=wp_sketch0.add(loop0).extrude(-0.04889812844749822)
