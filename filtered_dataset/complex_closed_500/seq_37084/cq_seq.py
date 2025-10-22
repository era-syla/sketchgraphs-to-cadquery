import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-3.43, 2.8).lineTo(0.0, 5.01164).lineTo(3.43, 2.8).lineTo(-3.43, 2.8).close()
solid=wp_sketch0.add(loop0).extrude(2.969436575314553)
