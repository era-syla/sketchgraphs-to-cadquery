import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-0.2413, 0.381).lineTo(0.2413, 0.381).lineTo(0.2413, -0.381).lineTo(-0.2413, -0.381).lineTo(-0.2413, 0.381).close()
solid=wp_sketch0.add(loop0).extrude(-1.0839702674083262)
