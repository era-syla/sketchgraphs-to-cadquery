import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-3.3, 0.1).lineTo(-0.1, 0.1).lineTo(-0.1, 3.3).lineTo(-3.3, 3.3).lineTo(-3.3, 0.1).close()
solid=wp_sketch0.add(loop0).extrude(-5.6286983848531555)
