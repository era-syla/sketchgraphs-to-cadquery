import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(0.0, 0.0).lineTo(0.0, 0.0415).lineTo(-0.022, 0.0415).lineTo(-0.022, 0.02603).lineTo(-0.0145, 0.01853).lineTo(-0.0145, 0.009).lineTo(-0.0175, 0.006).lineTo(-0.0175, 0.0).lineTo(0.0, 0.0).close()
solid=wp_sketch0.add(loop0).extrude(0.12321304375259311)
