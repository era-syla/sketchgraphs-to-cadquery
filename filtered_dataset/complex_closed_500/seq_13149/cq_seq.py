import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(0.0475, 0.03838).lineTo(-0.0475, 0.03838).lineTo(-0.0475, -0.03838).lineTo(0.0475, -0.03838).lineTo(0.0475, 0.03838).close()
solid=wp_sketch0.add(loop0).extrude(0.20127630092874468)
