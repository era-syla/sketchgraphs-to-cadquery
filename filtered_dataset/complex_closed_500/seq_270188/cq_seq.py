import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(0.2465, 0.2465).lineTo(-0.2465, 0.2465).lineTo(-0.2465, -0.2465).lineTo(0.2465, -0.2465).lineTo(0.2465, 0.2465).close()
solid=wp_sketch0.add(loop0).extrude(1.453457358935989)
