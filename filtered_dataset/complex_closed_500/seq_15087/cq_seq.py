import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(0.0, 0.0).lineTo(-4.572, 0.0).lineTo(-4.572, 3.048).lineTo(0.0, 3.048).lineTo(0.0, 0.0).close()
solid=wp_sketch0.add(loop0).extrude(-11.652301555765208)
