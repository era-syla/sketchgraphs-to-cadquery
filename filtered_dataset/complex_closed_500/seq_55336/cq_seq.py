import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-0.9652, 0.5334).lineTo(0.9652, 0.5334).lineTo(0.9652, -0.5334).lineTo(-0.9652, -0.5334).lineTo(-0.9652, 0.5334).close()
solid=wp_sketch0.add(loop0).extrude(-5.4918036971197095)
