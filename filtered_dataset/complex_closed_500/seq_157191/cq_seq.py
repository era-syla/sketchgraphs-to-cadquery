import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(0.5, 0.0).lineTo(0.0, 0.0).lineTo(0.0, -0.85).lineTo(0.5, -0.85).lineTo(0.5, 0.0).close()
solid=wp_sketch0.add(loop0).extrude(2.1979711799660655)
