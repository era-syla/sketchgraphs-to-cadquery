import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-0.4103, 0.3).lineTo(0.3897, 0.3).lineTo(0.3897, 0.0).lineTo(-0.4103, 0.0).lineTo(-0.4103, 0.3).close()
solid=wp_sketch0.add(loop0).extrude(-0.35701649393894463)
