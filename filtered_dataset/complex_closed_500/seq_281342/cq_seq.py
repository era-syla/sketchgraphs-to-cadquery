import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.0111, -0.14449).lineTo(-0.0073, -0.14449).lineTo(-0.0073, -0.23449).lineTo(-0.0111, -0.23449).lineTo(-0.0111, -0.14449).close()
solid=wp_sketch0.add(loop0).extrude(-0.19393300359095672)
