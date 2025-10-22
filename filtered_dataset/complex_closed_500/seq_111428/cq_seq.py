import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.0375, -0.022).lineTo(0.0375, -0.022).lineTo(0.0375, -0.05893).lineTo(-0.0375, -0.05893).lineTo(-0.0375, -0.022).close()
solid=wp_sketch0.add(loop0).extrude(-0.01986729512544494)
