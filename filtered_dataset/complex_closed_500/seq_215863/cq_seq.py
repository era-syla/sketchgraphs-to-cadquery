import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(0.00749, -0.02826).lineTo(-0.01477, -0.02826).lineTo(-0.01477, 0.02611).lineTo(0.00749, 0.02611).lineTo(0.00749, -0.02826).close()
solid=wp_sketch0.add(loop0).extrude(0.0716874783454782)
