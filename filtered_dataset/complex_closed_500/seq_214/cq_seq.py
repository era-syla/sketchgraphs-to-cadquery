import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.231, 0.002).lineTo(0.231, 0.002).lineTo(0.231, -0.002).lineTo(-0.231, -0.002).lineTo(-0.231, 0.002).close()
solid=wp_sketch0.add(loop0).extrude(0.42395737795257954)
