import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.01632, 0.002).lineTo(0.01868, 0.002).lineTo(0.01868, -0.023).lineTo(-0.01632, -0.023).lineTo(-0.01632, 0.002).close()
solid=wp_sketch0.add(loop0).extrude(-0.07621794744321347)
