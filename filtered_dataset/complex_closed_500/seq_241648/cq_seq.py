import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.0065, 0.00631).lineTo(0.01118, 0.00631).lineTo(0.01118, -0.05147).lineTo(-0.0065, -0.05147).lineTo(-0.0065, 0.00631).close()
solid=wp_sketch0.add(loop0).extrude(0.15490334994211527)
