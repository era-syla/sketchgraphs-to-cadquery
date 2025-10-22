import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-0.12124, 0.04788).lineTo(-0.12124, -0.05782).lineTo(-0.14843, -0.05782).lineTo(-0.14843, 0.04788).lineTo(-0.12124, 0.04788).close()
solid=wp_sketch0.add(loop0).extrude(0.25385397852909997)
