import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-0.08082, 0.07915).lineTo(0.02078, 0.07915).lineTo(0.02078, -0.02245).lineTo(-0.08082, -0.02245).lineTo(-0.08082, 0.07915).close()
solid=wp_sketch0.add(loop0).extrude(-0.12230228897975558)
