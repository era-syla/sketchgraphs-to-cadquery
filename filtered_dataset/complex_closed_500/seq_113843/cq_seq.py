import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.007, 0.032).lineTo(0.007, 0.032).lineTo(0.007, 0.0235).lineTo(-0.007, 0.0235).lineTo(-0.007, 0.032).close()
solid=wp_sketch0.add(loop0).extrude(-0.03750351110563944)
