import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.05715, 0.02858).lineTo(-0.05715, 0.02858).lineTo(-0.05715, -0.02858).lineTo(0.05715, -0.02858).lineTo(0.05715, 0.02858).close()
solid=wp_sketch0.add(loop0).extrude(-0.33408021899905355)
