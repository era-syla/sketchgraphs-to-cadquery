import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(1.15384, -0.39317).lineTo(1.21325, -0.39317).lineTo(1.21325, -0.48384).lineTo(1.15384, -0.48384).lineTo(1.15384, -0.39317).close()
solid=wp_sketch0.add(loop0).extrude(0.24602562259692284)
