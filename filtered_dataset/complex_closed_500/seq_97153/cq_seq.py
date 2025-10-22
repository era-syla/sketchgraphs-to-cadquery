import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.04934, 0.0).lineTo(0.13508, 0.0).lineTo(0.13508, -0.10435).lineTo(-0.04934, -0.10435).lineTo(-0.04934, 0.0).close()
solid=wp_sketch0.add(loop0).extrude(-0.10613704535682551)
