import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.045, 0.1).lineTo(0.045, 0.1).lineTo(0.045, 0.0).lineTo(-0.045, -0.0).lineTo(-0.045, 0.1).close()
solid=wp_sketch0.add(loop0).extrude(-0.1539443508099132)
