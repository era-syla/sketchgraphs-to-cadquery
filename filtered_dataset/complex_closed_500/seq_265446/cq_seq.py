import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-0.02105, 0.027).lineTo(0.00905, 0.027).lineTo(0.00905, 0.0165).lineTo(-0.02105, 0.0165).lineTo(-0.02105, 0.027).close()
solid=wp_sketch0.add(loop0).extrude(-0.04661919317086385)
