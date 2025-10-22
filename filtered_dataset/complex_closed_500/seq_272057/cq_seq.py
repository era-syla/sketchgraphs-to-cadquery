import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-0.50852, 0.28685).lineTo(-0.06581, 0.28685).lineTo(-0.06581, 0.0).lineTo(-0.50852, 0.0).lineTo(-0.50852, 0.28685).close()
solid=wp_sketch0.add(loop0).extrude(-0.9407624584277703)
